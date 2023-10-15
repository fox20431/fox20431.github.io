---
title: noise canceling for linux
date: 2023-10-14
---

# 消除Linux噪音

https://medium.com/@gamunu/linux-noise-cancellation-b9f997f6764d

## 安装插件

```shell
sudo pacman -S noise-suppression-for-voice
```

## Create Filter chain for PipeWire

```
mkdir -p ~/.config/pipewire/
vim ~/.config/pipewire/input-filter-chain.conf
```

配置文件

```
# Noise canceling source
#
# start with pipewire -c filter-chain/input-filter-chain.conf
#
context.properties = {
    log.level        = 0
}

context.spa-libs = {
    audio.convert.* = audioconvert/libspa-audioconvert
    support.*       = support/libspa-support
}

context.modules = [
    {   name = libpipewire-module-rtkit
        args = {
            #nice.level   = -11
            #rt.prio      = 88
            #rt.time.soft = 200000
            #rt.time.hard = 200000
        }
        flags = [ ifexists nofail ]
    }
    {   name = libpipewire-module-protocol-native }
    {   name = libpipewire-module-client-node }
    {   name = libpipewire-module-adapter }

    {   name = libpipewire-module-filter-chain
        args = {
            node.name =  "rnnoise_source"
            node.description =  "Noise Canceling source"
            media.name =  "Noise Canceling source"
            filter.graph = {
                nodes = [
                    {
                        type = ladspa
                        name = rnnoise
                        plugin = /usr/lib/ladspa/librnnoise_ladspa.so
                        label = noise_suppressor_stereo
                        control = {
                            "VAD Threshold (%)" 50.0
                        }
                    }
                ]
            }
            capture.props = {
                node.passive = true
            }
            playback.props = {
                media.class = Audio/Source
            }
        }
    }
]
```

## Persist the configuration

```
mkdir -p ~/.config/systemd/user/
vim ~/.config/systemd/user/pipewire-input-filter-chain.service
```

配置文件

```
[Unit]
Description=PipeWire Input Filter Chain
After=pipewire.service
BindsTo=pipewire.service

[Service]
ExecStart=/usr/bin/pipewire -c /home/<username>/.config/pipewire/input-filter-chain.conf
Type=simple
Restart=on-failure

[Install]
WantedBy=pipewire.service
```

## Reload systemd user unit files.

```
systemctl --user daemon-reload
systemctl --user enable pipewire-input-filter-chain.service
systemctl --user restart pipewire-input-filter-chain.service
systemctl --user status pipewire-input-filter-chain.service
```

