# 微信小程序指南🧭

相比较写Android，写微信小程序体验好太多了。

Android组为一个系统级别应用，是系统级程序，太过庞大，无论是开发还是编译。

而微信小程序本质上和网页差不多，但提供了微信从系统“借”来的权限。

但微信小程序提供了一站式解决方案。

## 准备

- 安装`微信开发者工具`（必选）
- 加入`微信客户端（开发开发者版）`（可选）

## TS支持

https://developers.weixin.qq.com/miniprogram/dev/devtools/compilets.html

JS迁移TS

在 project.config.json 文件中，修改 setting 下的 useCompilerPlugins 字段为 ["typescript"]，即可开启工具内置的 typescript 编译插件。 如需同时开启 less 编译插件，可将该字段修改为 ["typescript", "less"]。 目前支持三个编译插件：typescript、less、sass

```shell
npm install @types/wechat-miniprogram
```

https://www.npmjs.com/package/miniprogram-api-typings

如果之前的文件从 js 改为 ts，请清空缓存重新编译。

## 提示

### 版本

建议`微信开发者工具`和`微信`都更新到最新版本。

我不建议使用新的`base library`，不然远程调控会出现一堆报错，而且一些信息无法获取。

建议选择使用最多的`base library`。

### 项目配置

微信小程序的缩紧与`project.config.json`保持一致

```js
"editorSetting": {
	"tabIndent": "insertSpaces",
  "tabSize": 2
},
```

### 字体引用

**微信小程序有文件大小限制，font awesome太大，不要使用！！！**

微信小程序不支持 font 字体文件，需要将 font base 进行 base64 加密嵌入到文本中。

通过该网站 https://transfonter.org/ 可以将 font 进行 base64 嵌入到文本中。

