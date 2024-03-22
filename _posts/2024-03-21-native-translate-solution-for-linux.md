---
title: native translate solution for linux 
date: 2024-03-21
---

# Linux 平台本地翻译解决方案

离线翻译工具：argos-translate

```sh
argospm search
argospm install translate-en_zh
argospm install translate-zh_en
argos-translate --from en --to zh "hello"
```

text to speech：tts

```sh
pip install pip
pip-server --list_models
pip-server --model_name <model_name>
# e.g.
tts-server --model_name tts_models/en/vctk/vits
```

查词，用数据库

字典来源：https://github.com/skywind3000/ECDICT