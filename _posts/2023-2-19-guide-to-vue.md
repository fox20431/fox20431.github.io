# 从零开始的vue项目

vue 3 one piece

## 创建项目

该实例创建基于vite的vue项目

vite是vuejs的一个项目,用作服务器启动vue项目,目前仅适用于vue3.

vite相比webpack有着轻快的特点.

```sh
# npm创建命令
npm init vite-app <project-name>
# yarn创建命令
yarn create vite-app <project-name>
```

## 启动服务

进入目录
```sh
cd <project-name>
```

根据package.json安装相关依赖
```sh
npm install
# 或
yarn
```

启动服务
```sh
npm run dev
# 或
yarn dev
```

访问链接,看到vue页面即代表服务启动成功

## 认识包管理工具

包管理工具有npm和yarn.

两者作用相同,用于给项目安装依赖包.

```sh
# 安装
npm install package
yarn add package
# 卸载
npm uninstall package
yarn remove package
# 更新
npm install
yarn
# 等等
```

安装根据开发需要,如果需要将依赖打包进项目需要添加参数`--save`,如果不需要打包进项目则添加`--save-dev`;卸载不需要添加参数

hints: `npm install`可以简写成`npm i`, `npm uninstall`可以简写成`npm un`;npm和yarn的--save可以省略不写 --save-dev可以简写成-D


## 认识package.json

项目下根目录的`package.json`
```json
{
  "name": "demo",
  "version": "0.0.0",
  "scripts": {
    "dev": "vite",
    "build": "vite build"
  },
  "dependencies": {
    "vue": "^3.0.4",
  },
  "devDependencies": {
    "@vue/compiler-sfc": "^3.0.4",
    "vite": "^1.0.0-rc.13"
  }
}
```

它有很多属性:
- name
- version
- scripts
- dependencies
- devDependencies
- and so on

**name**是项目名称;
**version**是项目版本;
**scripts**是项目脚本,可以使用`yarn <key-name>`或者`npm run <key-name>`来执行命令;
**denpendencies**是项目依赖,打包会包含这部分内容;
**devDependencies**是项目开发依赖,打包不会包含这部分内容


## 添加依赖

yarn
```sh
# 依赖(dependencies)
yarn add package
# 开发依赖(devDependencies)
yarn add -D package
```

npm
```sh
# 依赖(dependencies)
npm i package
# 开发依赖(devDependencies)
npm i -D package
```

依赖推荐:
vue-router; 
vuex

## ts开发

用TypeScript语言来开发项目

安装依赖
```sh
yarn add -D typescript
```

项目根目录创建`tsconfig.ts`
```ts
declare module "*.vue" {
  import { defineComponent } from "vue";
  const Component: ReturnType<typeof defineComponent>;
  export default Component;
}
```

`src/main.js`重命名为`src/main.ts`

项目根目录`index.html`

```html
<script type="module" src="/src/main.js"></script> 
```
改为
```html
 <script type="module" src="/src/main.ts"></script>
```

## eslint语法

vscode插件:eslint语法检测工具,prettier格式化工具
eslint插件需要安装依赖
```sh
yarn add -D eslint eslint-plugin-vue@next
```
prettier可以独立运行

## UI库

Element UI：饿了吗

## VUE流程图

![vue flow chart](./assets/vue-flow-chart.svg)