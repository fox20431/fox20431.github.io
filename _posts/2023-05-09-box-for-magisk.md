# Box for Magisk

[Box for Magisk - GitHub](https://github.com/taamarin/box_for_magisk)

[Box for Magisk - Doc](https://github.com/taamarin/box_for_magisk/blob/master/docs/index_cn.md)


## Install the Moudle on Magisk

Download from GitHub Release

Install it on Magisk Modules

## Install Box Tools

```sh
su -c /data/adb/box/scripts/box.tool upyacd
su -c /data/adb/box/scripts/box.tool subgeo
su -c /data/adb/box/scripts/box.tool upcore
```

## Config

Box for Magisk supports multiple approaches to archive goals. To select the approach, you need to edit the config file located at `/data/adb/box/settings.ini`.

I will config `clash` as the proxy at the following step.

```sh
# select the proxy mode
proxy_mode="clash"
# set the network mode
network_mode="mixed" # change to mixed
```

Config clash services:

This is [a official tempalte](https://github.com/taamarin/box_for_magisk/blob/master/box/clash/config.yaml) for `clash`. I don't think anything related to **proxy server config** and **rule** should be modified.


## Control the service

Start the service

```sh
su -c /data/adb/box/scripts/box.service start
```

Stop the service

```sh
su -c /data/adb/box/scripts/box.service stop
```

Enable the tranparent proxy

```sh
su -c /data/adb/box/scripts/box.iptables enable
```

Disable the transparent proxy

```sh
su -c /data/adb/box/scripts/box.iptables disable
```

THERE BE DRAGON

The clash config will be appended `tun` config when we start the service using the mixed network mode.

If you have add the `tun` config, it will occur the conflict.
