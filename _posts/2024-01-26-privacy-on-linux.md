---
title: privacy on linux
date: 2024-01-26
---



check whether the microphone is used:

```
cat /proc/asound/card0/pcm0p/sub0/status
```



screenshare:

```
pw-dump | jq -r 'map(.info?.props?) | map(select(.["node.name"]? == "xdg-desktop-portal-wlr")) | map(.["stream.is-live"]? == true | "LIVE") | .[]?'
```

