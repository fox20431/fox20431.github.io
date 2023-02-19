注意：本文适用于bash，其他shell可能会存在差异。

shortcuts:

**manage process**

`ctrl - c`: terminate the current process

`ctrl - z`: suspend the current foreground process

`ctrl - d`: close the bash shell

`Ctrl + D`: Send an EOF marker, unless disabled by an option, this will close the current shell (EXIT).

**controll screen**

`ctrl - l`: clear the screen

`ctrl - s`: stop output to the screen

`ctrl - q`: resume output to screen

for example: 

```sh
sudo cat /dev/input/mice
```

it will output the information when the mice moved, it will stop print information when you use `ctrl - s`, use `ctrl - q` to resume output or `ctrl - c` stop precocess and resume output.

**move cousor**

`ctrl + a` or `HOME`: go to the beginning of the line

`ctrl + e` or `END`: go to the eng of the line

`alt - b`: go left (back) one word

`ctrl + b`: go left (back) one character

`alt + f`: go right (forward) one word

`ctrl + f`: go right (forward) one character

`ctrl + xx`: Move between the beginning of the line and the current position of the cursor.


**delete text**

`ctrl + d` or `DELETE`: delete the character under the cursor

`alt + d`: delete the word after the cursor

`ctrl + h` or `BACKSPACE`: delete the character before the cursor

`ctrl + w`: delete the word after the cursor

`ctrl - u`: delete the line before cursor

`ctrl - k`: delete the line after cursor

**cutting and paste**

`ctrl + w`: Cut the word before the cursor, adding it to the clipboard

`ctrl + k`: Cut the part of the line after the cursor, adding it to the clipboard

`ctrl + u`: Cut the part of the line before the cursor, adding it to the clipboard

`ctrl + y`: Paste the last thing you cut from the clipboard. The y here stands for “yank”   


**fixing typos**

`alt + t`: swap the current word with the previous word

`ctrl + t`: swap the current word with the previous word.

`ctrl + _`: undo your last key press

**capitalizing characters**

`alt + u`: capitalize a words from the cursor 

`alt + l`: uncapitalize a words from the cursor

`alt + c`: capitalize the character under the cursor

**command history**

`Ctrl + r`: Recall the last command including the specified character(s).

`Ctrl + p`: Previous command in history (i.e. walk back through the command history).

`Ctrl + n`: Next command in history (i.e. walk forward through the command history).

refer:

- https://www.howtogeek.com/howto/ubuntu/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/

- https://ss64.com/bash/syntax-keyboard.html
