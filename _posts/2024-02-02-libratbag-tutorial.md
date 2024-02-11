---
title: libratbag tutorial
date: 2024-02-02
---

# Libratbag Tutorial



```sh
sudo pacman -S libratbag
sudo systemctl enable ratbagd
sudo systemctl restart ratbagd
```



list devices:

```sh
ratbagctl list
```

show current dpi

```sh
ratbagctl "<devcie_name>" dpi get
# for example
ratbagctl "Logitech G304" dpi get
```

