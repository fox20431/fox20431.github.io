# Visual Studio Code

Visual Studio Code 可以设置全局配置文件，通过 cmd + , 快捷键修改setting.json文件。

同时你也可以为项目设置`${root}/.vscode/settings.json`（`${root}`是项目根目录）。

项目配置优先级高于全局配置。

## Palette

`${filename}`
`>${command}` command
`:${number}` jump line


## Variable

vscode 预定义了许多变量

https://code.visualstudio.com/docs/editor/variables-reference

- **${userHome}** - the path of the user's home folder
- **${workspaceFolder}** - the path of the folder opened in VS Code
- **${workspaceFolderBasename}** - the name of the folder opened in VS Code without any slashes (/)
- **${file}** - the current opened file
- **${fileWorkspaceFolder}** - the current opened file's workspace folder
- **${relativeFile}** - the current opened file relative to `workspaceFolder`
- **${relativeFileDirname}** - the current opened file's dirname relative to `workspaceFolder`
- **${fileBasename}** - the current opened file's basename
- **${fileBasenameNoExtension}** - the current opened file's basename with no file extension
- **${fileDirname}** - the current opened file's dirname
- **${fileExtname}** - the current opened file's extension
- **${cwd}** - the task runner's current working directory upon the startup of VS Code
- **${lineNumber}** - the current selected line number in the active file
- **${selectedText}** - the current selected text in the active file
- **${execPath}** - the path to the running VS Code executable
- **${defaultBuildTask}** - the name of the default build task
- **${pathSeparator}** - the character used by the operating system to separate components in file paths

系统的环境变量：${env:USERNAME}

vscode配置的变量：${config:editor.fontSize}

${command:commandID}

tasks.json

```json
{
	"version": "2.0.0",
	"tasks": [
		{
			"label": "node executor",
			"type": "shell",
			"command": "node",
			"args": [
				"${file}"
			],
			"group": "build"
		}
	]
}
```

