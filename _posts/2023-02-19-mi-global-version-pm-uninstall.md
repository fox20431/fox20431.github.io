commands:
adb shell pm list packages
adb shell pm uninstall --user 0 应用包名
adb shell pm disable --user 0 应用包名

MIUI系统国内版可卸载软件（测试删除后能正常开机使用）：
adb shell pm uninstall --user 0 com.miui.systemAdSolution  （小米系统广告解决方案，必删）
adb shell pm uninstall --user 0 com.miui.analytics  （小米广告分析，必删）
adb shell pm uninstall --user 0 com.xiaomi.gamecenter.sdk.service  （小米游戏中心服务）
adb shell pm uninstall --user 0 com.xiaomi.gamecenter  （小米游戏中心）
adb shell pm uninstall --user 0 com.sohu.inputmethod.sogou.xiaomi  （搜狗输入法）
adb shell pm uninstall --user 0 com.baidu.input_mi （百度输入法小米版）
adb shell pm uninstall --user 0 com.miui.player  （小米音乐）
adb shell pm uninstall --user 0 com.miui.video  （小米视频）
adb shell pm uninstall --user 0 com.miui.notes  （小米便签）
adb shell pm uninstall --user 0 com.miui.translation.youdao  （有道翻译）
adb shell pm uninstall --user 0 com.miui.translation.kingsoft  （金山翻译）
adb shell pm uninstall --user 0 com.android.email  （邮件）
adb shell pm uninstall --user 0 com.xiaomi.scanner  （小米扫描）
adb shell pm uninstall --user 0 com.miui.hybrid  （混合器）
adb shell pm uninstall --user 0 com.miui.bugreport  （bug 反馈）
adb shell pm uninstall --user 0 com.milink.service  （米连服务）
adb shell pm uninstall --user 0 com.android.browser  （浏览器）
adb shell pm uninstall --user 0 com.miui.gallery  （相册）
adb shell pm uninstall --user 0 com.miui.yellowpage  （黄页）
adb shell pm uninstall --user 0 com.xiaomi.midrop  （小米快传）
adb shell pm uninstall --user 0 com.miui.virtualsim  （小米虚拟器）
adb shell pm uninstall --user 0 com.xiaomi.payment  （小米支付）
adb shell pm uninstall --user 0 com.mipay.wallet  （小米钱包）
adb shell pm uninstall --user 0 com.android.soundrecorder  （录音机）
adb shell pm uninstall --user 0 com.miui.screenrecorder  （屏幕录制）
adb shell pm uninstall --user 0 com.android.wallpaper  （壁纸）
adb shell pm uninstall --user 0 com.miui.voiceassist  （语音助手）
adb shell pm uninstall --user 0 com.miui.fm  （收音机）
adb shell pm uninstall --user 0 com.miui.touchassistant  （悬浮球）
adb shell pm uninstall --user 0 com.android.cellbroadcastreceiver  （小米广播）
adb shell pm uninstall --user 0 com.xiaomi.mitunes  （小米助手）
adb shell pm uninstall --user 0 com.xiaomi.pass  （小米卡包）
adb shell pm uninstall --user 0 com.android.thememanager  （个性主题管理）
adb shell pm uninstall --user 0 com.android.wallpaper  （动态壁纸）
adb shell pm uninstall --user 0 com.android.wallpaper.livepicker  （动态壁纸获取）
adb shell pm uninstall --user 0 com.miui.klo.bugreport  （KLO bug 反馈）

MIUI国际版应用包名（欧版可以随便删）：

adb shell pm uninstall --user 0 com.google.android.googlequicksearchbox （Google快速搜索框）

adb shell pm uninstall --user 0 com.miui.miservice  （服务与反馈）

adb shell pm uninstall --user 0 com.mi.health   （小米健康）

adb shell pm uninstall --user 0 com.mi.globalbrowser    （小米国际版浏览器）

adb shell pm uninstall --user 0 com.miui.huanji （小米换机）

adb shell pm uninstall --user 0 com.miui.newmidrive （小米云盘）

adb shell pm uninstall --user 0 com.miui.bugreport  （用户反馈）
adb shell pm uninstall --user 0 com.miui.personalassistant  （智能助理）
adb shell pm uninstall --user 0 com.android.hotwordenrollment.xgoogle   （谷歌助理1）
adb shell pm uninstall --user 0 com.android.hotwordenrollment.okgoogle  （谷歌助理2）
adb shell pm uninstall --user 0 com.xiaomi.mirecycle    （小米回收）
adb shell pm uninstall --user 0 com.miui.videoplayer    （小米视频国际版）

adb shell pm uninstall --user 0 com.miui.player（小米音乐）

adb shell pm uninstall --user 0 com.google.android.projection.gearhead  （Google Auto/Google 汽车）
adb shell pm uninstall --user 0 com.google.android.gms.location.history （Google 地理位置历史记录）
adb shell pm uninstall --user 0 com.google.ar.lens  （Google 智能（虚拟）摄像头）
adb shell pm uninstall --user 0 cn.wps.moffice_eng.xiaomi.lite  （小米轻量版WPS）

adb shell pm uninstall --user 0 com.mfashiongallery.emag（小米画报）

adb shell pm uninstall --user 0 com.android.updater (小米更新，有点卡卸载了，之后通过twrp更新)

```
adb shell pm uninstall --user 0 com.android.hotwordenrollment.xgoogle
adb shell pm uninstall --user 0 com.android.hotwordenrollment.okgoogle
adb shell pm uninstall --user 0 com.google.android.projection.gearhead
adb shell pm uninstall --user 0 com.google.android.gms.location.history
adb shell pm uninstall --user 0 com.google.ar.lens
adb shell pm uninstall --user 0 com.miui.videoplayer
adb shell pm uninstall --user 0 com.miui.player
adb shell pm uninstall --user 0 com.xiaomi.scanner
adb shell pm uninstall --user 0 com.android.updater
adb shell pm uninstall --user 0 com.android.fileexplorer
adb shell pm uninstall --user 0 com.android.email
adb shell pm uninstall --user 0 com.android.providers.downloads.ui
adb shell pm uninstall --user 0 com.mi.health

adb shell pm uninstall --user 0 com.xiaomi.mirecycle
adb shell pm uninstall --user 0 com.xiaomi.payment
adb shell pm uninstall --user 0 com.miui.huanji
adb shell pm uninstall --user 0 com.miui.miservice
adb shell pm uninstall --user 0 com.mi.globalbrowser
adb shell pm uninstall --user 0 com.miui.newmidrive
adb shell pm uninstall --user 0 cn.wps.moffice_eng.xiaomi.lite
adb shell pm uninstall --user 0 com.mfashiongallery.emag
adb shell pm uninstall --user 0 com.miui.bugreport
adb shell pm uninstall --user 0 com.xiaomi.mirror
```

MIUI 国内版系统会在开机前检查下面一些关键应用和服务（包括但不限于），若被卸载或冻结，则开不了机——俗称「卡米」；MIUI 国际版则取消了这个限制。
com.miui.cloudservice   （小米云服务）
com.xiaomi.account  （小米账户）
com.android.updater （系统更新）
com.miui.cloudbackup    （云备份）
com.xiaomi.market   （应用市场）

参考：https://fengooge.blogspot.com/2019/03/taking-ADB-to-uninstall-system-applications-in-MIUI-without-root.html