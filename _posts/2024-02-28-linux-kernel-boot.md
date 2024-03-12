# Linux Kernel Boot

## EFI stub

**TL;DR**

以 `gentoo` 为例。`/efi` 为 `ESP` 分区的挂载点。

1. 拷贝编译内核生成的 `./arch/x86/boot/bzImage` 到 `/boot/EFI/gentoo/bzImage.efi`；
2. 用 `dracut` 生成 `initramfs(AKA. initrc)` 到 `/efi/EFI/gentoo/initrd.cpio.gz`：
    ```sh
    dracut /efi/EFI/gentoo/initrd.cpio.gz --kver <kernel_version>
    # 这个 kernel_version 可以通过 ls /lib/modules 来查看
    ```
3. 用 `efibootmgr` 注册相关信息（根目录uuid以及initrd）：
    ```sh
    efibootmgr --create --disk /dev/nvme1n1 --label "Gentoo" --loader "\EFI\gentoo\bzImage.efi" -u 'root=UUID=97ffc05a-6098-4af9-9d61-a40f403fffca initrd=\EFI\gentoo\initrd.cpio.gz'
    ```

refer: 

- [gentoo efi stub](https://wiki.gentoo.org/wiki/EFI_stub#Installation)
- [gentoo reply about efi stub](https://forums.gentoo.org/viewtopic-p-8805827.html#8805827)

以下内容摘录 [gentoo reply about efi stub](https://forums.gentoo.org/viewtopic-p-8805827.html#8805827) 并稍作修改：

**first of all**: UEFI starts a binary (not a partition), this can be a bootloader (like grub) or a Linux kernel (or Windows). UEFI can start a binary ONLY from an ESP (efi system partition), so, this binary file MUST be on your ESP, additionally your UEFI needs the information which binary it shall start. This is an UEFI boot entry. You can see these boot entries with "efibootmgr", and also change, add or delete them with it.

Now what is necessary to boot a kernel directly:

1. Your BIOS setting must allow UEFI boot (this is OK because you start the grub with UEFI)
2. Your harddisk must have GPT (instead MBR) - this is also OK because you start the grub with UEFI
3. On your harddisk you must have a partition with ESP flag enabled: Your ESP (also OK)
4. This partition must be formatted with a FAT variant (recommended: FAT32) ... also OK
5. On this partition must be a directory named \EFI (or \efi because we have FAT and dont care if it is uppercase or lowercase) ... dont forget: If you mount this partition in a Linux system to a directory like /boot you will SEE IT as: /boot/EFI
6. In this \EFI directory you make another directory ... like \EFI\gentoo ... or \EFI\example ... or \EFI\backup
7. Your kernel must be configured to "be" a STUB kernel.
8. In this directory you MUST copy the binary file you want to start ... AND ... this file must have the suffix .efi. If you install grub then the Gentoo grub-install-routine installs your grub into \EFI\gentoo\grubx64.efi ... If you want start your stub kernel then you MUST copy the kernel (from where it was build; maybe: /usr/src/linux/arch/x86/boot/bzImage) into this directory. Example:

```sh
mount /dev/nvme0n1p1 /boot
mkdir -p /boot/EFI/example
cp /usr/src/linux/arch/x86/boot/bzImage /boot/EFI/example/bzImage.efi
```

(with this copy you also rename your kernel to have suffix .efi)
9. Now you need a UEFI boot entry. Do this with "efibootmgr" ... Because UEFI see only the ESP as FAT parition you must use BACKSLASHES (and no /boot because this is a directory of your root partition. UEFI sees only your ESP directly and the "FIRST" directory UEFI see is: \EFI). Example:

```
efibootmgr --create --disk /dev/nvme0n1 --label "Gentoo" --part 1 --loader "\EFI\example\bzImage.efi"	
```
Yes, there was missing the first \ in --loader "EFI\BOOT\bzImage.efi'
(hint: When you create a new boot entry with "efibootmgr" then "efibootmgr automatically changes the boot order: So, your new created entry is the FIRST entry UEFI will boot.)

... Now ... with this you can start a kernel ... BUT ... a kernel needs one information: Where is my root partition ? Here you have two choices:

a) You can configure it into the kernel (as "Built-in kernel command line"), OR
b) UEFI passes the information as kernel command line parameter to the kernel. THIS is be done when you create the UEFI boot entry ... you ADD this parameter with option -u

(supplement: if you are using grub as bootloader, then it is the job of grub to pass this information to the kernel)

Example:

```sh
efibootmgr --create --disk /dev/nvme0n1 --label "Gentoo" --part 1 --loader "\EFI\example\bzImage.efi" -u "root=/dev/nvme0n1p3"	
```
**BUT THAT IS NOT ALL**

You can have a kernel WITH or WITHOUT an initramfs ...

If you configure your kernel yourself you can renounce to build an initramfs ... but if you are using a DIST-kernel (or you made it with genkernel) THEN you have an initramfs ...

... AND now you MUST configure UEFI so it passes this initramfs ALSO to your kernel. You must do - additionally - two steps:

1. Copying this initramfs-file ALSO into /boot/EFI/example ... AND
2. Telling UEFI where to find ... this you do also with parameter -u

Example:
Code:

```sh	
efibootmgr --create --disk /dev/nvme0n1 --label "Gentoo" --part 1 --loader "\EFI\example\bzImage.efi" -u "root=/dev/nvme0n1p3 initrd=\EFI\example\initramfs.CPIO"	
```


If your ESP is the first partition, then you can omit the --part 1 specification (because -p 1 is default). You can also shorten it, e.g.:
Code:	

```sh
efibootmgr -c -d /dev/nvme0n1 -L "Gentoo" -l "\EFI\example\bzImage.efi" -u "root=/dev/nvme0n1p3 initrd=\EFI\example\initramfs.CPIO"	
```

Instead initramfs.CPIO use the name of your copied initramfs ! (You can use as parm -L what you like; this is the name you will see in your BIOS; I named one of my entries "Secure" and the other "Backup"; If you have already an entry with name "Gentoo" you should use another name).

Attention: If you think you configure both parameters into the kernel ...

Code:	

```
Processor type and features  --->
    [*] Built-in kernel command line
    (root=/dev/nvme0n1p3 ro initrd=\EFI\example\initramfs.CPIO)	
```


together with:
Code:	

```sh
efibootmgr -c -d /dev/nvme0n1 -L "Gentoo" -l "\EFI\example\bzImage.efi"	
```

... This does not work !

You can configure your root= into the kernel, but the information initrd= MUST be a UEFI parameter. So, IF you have in your kernel command line:

```
Processor type and features  --->
    [*] Built-in kernel command line
    (root=/dev/nvme0n1p3 ro)	
```

You MUST make an UEFI entry so:

```sh
efibootmgr -c -d /dev/nvme0n1 -L "Gentoo" -l "\EFI\example\bzImage.efi" -u "initrd=\EFI\example\initramfs.CPIO"	
```

See more here:
https://wiki.gentoo.org/wiki/User:Pietinger/Tutorials/Kernel_Commandline_Parameter


You have asked about kernel options ...

1. Your kernel must - ALWAYS - be able to access a GPT parititon (independent if you want use your kernel as stub kernel or not; as soon as you have GPT every kernel must have this config). This is explained in: https://wiki.gentoo.org/wiki/EFI_System_Partition
(Every dist-kernel has this already configured/enabled in the kernel; so, no need to do it 8) )
2. Your kernel must be a STUB kernel if you want boot it directly. This is explained in: https://wiki.gentoo.org/wiki/EFI_stub
3. If you want access UEFI variables (with "efibootmgr") your kernel needs access to it. This is explained in: https://wiki.gentoo.org/wiki/Efibootmgr
(If you are funny you can have a stub kernel without these settings ... but you can never do "efibootmgr" :lol: ... you see this is also independent if you build a stub kernel; also a "normal" kernel needs this if you want start 

