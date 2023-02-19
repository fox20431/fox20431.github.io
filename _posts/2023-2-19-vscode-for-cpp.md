# Visual Studio Code For Cpp

## Mac Config

.vscode/c_cpp_properties.json

```json
{
    "configurations": [
        {
            "name": "Mac",
            "includePath": [
                "${workspaceFolder}/**",
                "${workspaceFolder}"
            ],
            "defines": [],
            "macFrameworkPath": [
                "/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/System/Library/Frameworks"
            ],
            "compilerPath": "/usr/bin/clang",
            "cStandard": "c17",
            "cppStandard": "c++20",
            "intelliSenseMode": "macos-clang-x64",
            "configurationProvider": "ms-vscode.cmake-tools"
        }
    ],
    "version": 4
}
```

.vscode/tasks.json

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "type": "cppbuild",
            "label": "build active file",
            "command": "/usr/bin/clang++",
            "args": [
                // need to add `-g`, or debug not working!
                "-g",
                "${file}",
                "-o",
                "${workspaceFolder}/build/${fileBasenameNoExtension}"
            ],
            "options": {
                "cwd": "${fileDirname}"
            },
            "problemMatcher": [
                "$gcc"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "detail": "Build active C/C++ file"
        }
    ]
}
```

.vscode/launch.json

```json
{
	"version": "0.2.0",
	"configurations": [
		{
			"name": "(lldb) Launch",
			"preLaunchTask": "build active file",
			"type": "cppdbg",
			"request": "launch",
			"program": "${workspaceFolder}/build/${fileBasenameNoExtension}",
			"args": [],
			"stopAtEntry": false,
			"cwd": "${fileDirname}",
			"environment": [],
			// use external console
			"externalConsole": true,
			"MIMode": "lldb"
		}
	],
}
```

