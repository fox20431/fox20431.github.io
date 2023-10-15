---
title: common shell
date: 2023-10-13
---

# Common Shell

upgrade all python packages with pip

```bash
pip --disable-pip-version-check list --outdated --format=json | python -c "import json, sys; print('\n'.join([x['name'] for x in json.load(sys.stdin)]))" | xargs -n1 pip install -U
```