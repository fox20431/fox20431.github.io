title: linux audio
date: 2024-02-20
---

# Linux 音量

电脑声卡是 Realtek ，但是 Linux 显示的声卡是 Intel HDA ，这是为什么？

参考 [The ArchLinux Post](https://bbs.archlinux.org/viewtopic.php?id=243515)：

> Realtek chipsets all are part of the HDA standard and are usually all implemented onboard, what makes you think that the card you're seeing isn't just that? More of interest would be the codec which will likely point to some realtek device, what's your output of

使用如下命令可以查看相关日志：

```sh
dmesg | grep snd
```

以下是输出：

```log
[    6.256792] snd_hda_intel 0000:00:1f.3: DSP detected with PCI class/subclass/prog-if info 0x040100
[    6.256869] snd_hda_intel 0000:00:1f.3: Digital mics found on Skylake+ platform, using SOF driver
[    6.990784] snd_hda_codec_realtek ehdaudio0D0: autoconfig for ALC257: line_outs=1 (0x14/0x0/0x0/0x0/0x0) type:speaker
[    6.990786] snd_hda_codec_realtek ehdaudio0D0:    speaker_outs=0 (0x0/0x0/0x0/0x0/0x0)
[    6.990787] snd_hda_codec_realtek ehdaudio0D0:    hp_outs=1 (0x21/0x0/0x0/0x0/0x0)
[    6.990788] snd_hda_codec_realtek ehdaudio0D0:    mono: mono_out=0x0
[    6.990788] snd_hda_codec_realtek ehdaudio0D0:    inputs:
[    6.990789] snd_hda_codec_realtek ehdaudio0D0:      Mic=0x19
```

通过 `autoconfig for ALC257` 可以看出默认指向了 Realtek ALC257 这个声卡。