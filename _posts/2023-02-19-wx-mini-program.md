# 微信小程序

第一次进入页面会加载 onLoad 和 onShow

## 开发前须知

### 小程序运行环境

Reference: https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/env.html

微信小程序运行在多种平台上：iOS/iPadOS 微信客户端、Android 微信客户端、Windows PC 微信客户端、Mac 微信客户端、[小程序硬件框架](https://developers.weixin.qq.com/doc/oplatform/Miniprogram_Frame/)和用于调试的微信开发者工具等。

不同运行环境下，脚本执行环境以及用于组件渲染的环境是不同的，性能表现也存在差异：

- 在 iOS、iPadOS 和 Mac OS 上，小程序逻辑层的 JavaScript 代码运行在 JavaScriptCore 中，视图层是由 WKWebView 来渲染的，环境有 iOS 14、iPad OS 14、Mac OS 11.4 等；
- 在 Android 上，小程序逻辑层的 JavaScript 代码运行在 [V8](https://developers.google.com/v8/) 中，视图层是由基于 Mobile Chromium 内核的微信自研 XWeb 引擎来渲染的；
- 在 Windows 上，小程序逻辑层 JavaScript 和视图层都是用 Chromium 内核；
- 在 开发工具上，小程序逻辑层的 JavaScript 代码是运行在 [NW.js](https://nwjs.io/) 中，视图层是由 Chromium Webview 来渲染的。

了解小程序运行环境可以使得我们针对语言特定平台以及特性开发。

### 宿主环境

https://developers.weixin.qq.com/miniprogram/dev/framework/quickstart/framework.html

## 开发

### 了解生命周期



