# Create React from Scratch

## 前言

构建 React 除了从零构建也可以通过脚手架自动构建，后者方式会受到CRA（create-react-app）限制，比如他打包的版本老旧。当安装第三方包时，会出现不兼容的情况。我在使用CRA创建项目时，遇到安装SASS后不能使用，当我使用yarn check时，发现SASS需要Webpack5版本，而脚手架安装的是4版本的，由于CRA添加的大多数包不熟悉，导致我很难进行修复。

```sh
npx create-react-app my-app
cd my-app
npm start
# or
yarn create react-app my-app
cd <app-name>
npm start
```

## 依赖

依赖会被放入`package.json`包中，下面介绍一些主要的依赖及其配置。

### webpack

```sh
yarn add -D webpack webpack-cli webpack-dev-server 
```

webpack：打包工具，可以将各种资源进行打包。

webpack-dev-server：开发过程中搭建测试服务（即将你写的代码整合起来放到网页上来看预期效果）

webpack-cli：webpack的命令行包，包括许多命令行，具体见`npx webpack-cli --help`。

### webpack plugin

doc: https://webpack.js.org/plugins/html-webpack-plugin/

simplifies creation of HTML files to serve your webpack bundles.

```sh
yarn add -D html-webpack-plugin
```

通过该插件指定html文件服务js文件。比如react项目的js文件需要挂载html的节点，一般情况下并不会自动打包被挂载目标html文件，因此生成的文件缺少html文件，自然无法通过浏览器访问，使用这个工具就可以解决这个问题。

### webpack loader

#### type script

```sh 
yarn add -D typescript ts-loader
```

配置ts

tsconfig.json

```json
{
	"compilerOptions": {
	  "outDir": "./dist/",
	  "noImplicitAny": true,
	  "module": "es6",
	  "target": "es5",
	  "jsx": "react",
	  "allowJs": true,
	  "moduleResolution": "node"
	}
}
```

为了能让ts能够在文件中引入其他类型文件，项目根目录创建`declaration.d.ts`文件（文件名xxx.d.ts）并写入：

```ts
// TypeScript does not know that there are files other than .tsor .tsx.
declare module '*.css';
```

#### react

```sh
yarn add react react-dom react-router react-router-dom
yarm add -D @types/react @types/react-dom @types/react-router @types/react-router-dom
```

配置ts头

```sh
yarn add -D @types/react @types/react-dom
```

#### babel

Babel作为语法解析器，他可以将不同协议版本的js(/ts/jsx/tsx)解析成浏览器支持的协议版本。

```sh
yarn add -D @babel/core @babel/cli @babel/preset-env @babel/preset-typescript @babel/preset-react babel-loader
```

- @babel/preset-env for compiling ES2015+ syntax 
- @babel/preset-typescript for TypeScript 
- @babel/preset-react for React 
- @babel/preset-flow for Flow

在根目录建立`.babelrc`文件，然后写入以下配置

```json
{
	"presets": [
			"@babel/preset-env",
			"@babel/preset-react",
			"@babel/preset-typescript"
	]
}
```

doc: https://babeljs.io/docs/en/config-files#project-wide-configuration

#### html

```sh
yarn add -D html-loader
```

#### Style

其中css-loader是必需的，它的作用是解析CSS文件，包括解析@import等CSS自身的语法。它的作用也仅仅是解析CSS文件，它会把CSS文件解析后，以字符串的形式打包到JS文件中。不过，此时的CSS样式并不会生效，因为我们需要把CSS插入到html里才会生效。

此时，style-loader就来发挥作用了，它可以把JS里的样式代码插入到html文件里。它的原理很简单，就是通过JS动态生成style标签插入到html文件的head标签里。

```sh
yarn add --dev css-loader style-loader
```

如果需要sass可以添加

```sh
yarn add --dev node-sass sass-loader
```

through sass-loader -> css-loader -> style-loader

#### 其他

如果你需要其他的，比如阿里基于react的样式，你可以下载antd包。

### 最终模板

react+sass

目录结构

```
├── package.json
├── src
│   ├── App.jsx
│   ├── index.html
│   ├── index.js
├── webpack.config.js
└── yarn.lock
```

/package.json

```json
{
  "devDependencies": {
    "@babel/cli": "^7.17.10",
    "@babel/core": "^7.18.2",
    "@babel/preset-env": "^7.18.2",
    "@babel/preset-react": "^7.17.12",
    "@types/react": "^18.0.11",
    "@types/react-dom": "^18.0.5",
    "babel-loader": "^8.2.5",
    "css-loader": "^6.7.1",
    "html-loader": "^3.1.0",
    "html-webpack-plugin": "^5.5.0",
    "style-loader": "^3.3.1",
    "ts-loader": "^9.3.0",
    "typescript": "^4.7.3",
    "webpack": "^5.72.1",
    "webpack-cli": "^4.9.2",
    "webpack-dev-server": "^4.9.0"
  },
  "dependencies": {
    "@microsoft/office-js": "^1.1.73",
    "@reduxjs/toolkit": "^1.8.2",
    "react": "^18.1.0",
    "react-dom": "^18.1.0",
    "react-redux": "^8.0.2",
    "react-router": "^6.3.0",
    "react-router-dom": "^6.3.0",
    "redux": "^4.2.0"
  }
}
```

/webpack.config.js

```js
const path = require('path');
// The plugin will generate an HTML5 file for you that includes all your webpack bundles in the head using script tags.
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
    entry: path.resolve(__dirname, 'src/index.tsx'),
    output: {
        filename: 'bundle.js',
        // default public is root, it will impact url when you modify it.
        // publicPath: '/'
        path: path.resolve(__dirname, 'dist'),
    },
    // generate js mapping files to facilitate debugging.
    devtool: 'source-map',
    mode: 'development',
    resolve: {
        // Add `.ts` and `.tsx` as a resolvable extension.
        extensions: [".js", '.jsx', '.ts', '.tsx']
    },
    // module will add loaders to transfer various assets.
    module: {
        rules: [
            {
                test: /\.html$/i,
                use: 'html-loader'
            },
            {
                test: /\.css$/i,
                use: [ // through css-loader -> style-loader
                    {
                        // Translates CSS into CommonJS
                        loader: 'css-loader',
                    },
                    {
                        // Creates `style` nodes from JS strings
                        loader: 'style-loader',
                    }
                ],
            },
            {
                test: /\.jsx?$/,
                use: 'babel-loader',
                exclude: /node_modules/

            },
            {
                test: /\.tsx?$/,
                use: 'ts-loader',
                exclude: /node_modules/,
            },
            {
                test: /\.(png|jpe?g|svg)/,
                // raw-loader, url-loader, file-loader is deprecated in webpack5.
                // please use asset, or appear bug of loading css picture.
                // more info please check: https://webpack.js.org/guides/asset-modules/
                type: 'asset/resource'
            }
        ]
    },
    devServer: {
        port: 3000,
        compress: true,
        // hot swap
        hot: true,
        // make BrowserRouter work
        historyApiFallback: true,
    },
    plugins: [
        new HtmlWebpackPlugin({
            // select html file that the react-dom will mount.
            template: path.resolve(__dirname, 'src/index.html'),
            filename: 'index.html'
        }),
    ],
    performance: {
        // Webpack hints message when the generated JavaScript File is larger than preset.
        hints: false,
    },
};
```

/src/index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./style/reset.css">
    <title>index</title>
</head>
<body>
    <div id="root"></div>
</body>
</html>
```

### 管理项目

运行项目

```sh
npx webpack-dev-server
# or
npx webpack-cli s
# or
yarn webpack-dev-server
# or
yarn webpack-cli s
```

打包项目

```sh
npx webpack
# or
npx webpack-cli b
# or
yarn webpack
# or
yarn webpack-cli b
```
