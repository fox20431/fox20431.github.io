# MineCraft

我的世界


## Mod

安装 [Fabric](https://fabricmc.net/) 。

安装完成后会在 Minecraft Launcher 上新增 `fabirc-loader-<version>` 的游戏版本选项。

如果你有想加载的模组，将其拖入到 `C:\Users\<USERNAME>\AppData\Roaming\.minecraft\mods` 下即可。

模组聚合网站：[CurseForge](https://www.curseforge.com/minecraft/mc-mods)

Fobric 的模组有的需要 `Fobric API` ，所以这个API应该被安装。

其他推荐的模组：

- Neat：查看血量模组
- MiniHUD：辅助显示区域，查看需要安装 `MaLiLib`

## Server


[官方下载连接](https://www.minecraft.net/zh-hans/download/server?spm=a2c4e.10696291.0.0.31c119a4bK5UmZ)

推荐使用的命令：

```
nohup java -Xmx1024M -Xms1024M -jar minecraft_server.1.19.3.jar nogui >> main.log &
```
