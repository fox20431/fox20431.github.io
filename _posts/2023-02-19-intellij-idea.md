## Common Question

卡在首屏界面的的解决方案：

> Please try to add the option `-Dide.browser.jcef.enabled=false` to `~/.config/JetBrains/IntelliJIdea2020.3/`idea64.vmoptions

refer: https://youtrack.jetbrains.com/issue/IDEA-253459/buffer-overflow-detected-when-importing-a-project


## springboot devtools热交换

1. build, execution, deploy > compiler > check 'compile independent automatically'

2. advanced settings > check 'allow auto-make to start ...'