---
title: git data masking
date: 2023-12-18
---

# Git 信息脱敏

可以针对hooks的`pre-commit`和`post-commit`两个文件作做关于信息脱敏的操作：

```sh
#!/bin/bash

echo "This is the global pre-commit hook!"

# Iterate over all staged files
git diff --cached --name-only | while read -r file; do
    # Replace "foo" with "bar" in each staged file
    sed -i 's/foo/bar/g' "$file"
	# ...
done

# Stage the changes
git add .
```

同时如果为了不影响当前的操作，需要脱敏后修改回来：

```sh
#!/bin/bash

echo "This is the global post-commit hook!"

# Iterate over all staged files
git log --name-only --oneline -1 | while read -r file; do
    sed -i 's/bar/foo/g' "$file"
    # ...
done

# Stage the changes
git add .
```

由于钩子并不会提交上去，因此不用担心自己的替换的字符串被看到。