# Visual Studio Code For Java


## Preface

```sh
sudo pacman -S jre17-openjdk-headless jre17-openjdk openjdk17-doc openjdk17-src
```

## Config

Java 开发 VSCode

```json
"java.autobuild.enabled": true,
"java.configuration.runtimes": [
		{
			"name": "JavaSE-11",
			"path": "${JAVA_11_HOME}"
		},
		{
			"name": "JavaSE-17",
			"path": "${JAVA_17_HOME}",
			"sources": "${JAVA_17_HOME}/lib/src.zip",
            "javadoc": "https://docs.oracle.com/en/java/javase/17/docs/api",
			"default": true
		}
	],
```

`java.configuration.runtimes.name` 必须填写提供的字符串

`java.configuration.runtimes.path`为`JAVA_HOME`的绝对路径，如果你在操作系统的环境变量中制定了`JAVA_HOME`也可以通过`${JAVA_HOME}`来引用环境变量

`java.configuration.runtimes.sources`用于指定源文件`zip`压缩包的路径。

`java.configuration.runtimes.javadoc`指定文档位置，来源可以为本地也可以为网络

