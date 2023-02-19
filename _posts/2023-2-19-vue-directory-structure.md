```shell
├── build/               # Webpack 配置目录
├── dist/                # build 生成的生产环境下的项目
├── config/               # Vue基本配置文件，可以设置监听端口，打包输出等
├── node_modules/                # 依赖包，通常执行npm i会生成
├── src/                 # 源码目录（开发的项目文件都在此文件中写）
│   ├── assets/            # 放置需要经由 Webpack 处理的静态文件，通常为样式类文件，如css，sass以及一些外部的js
│   ├── components/        # 公共组件
│   ├── filters/           # 过滤器
│   ├── store/    　　　　 # 状态管理
│   ├── routes/            # 路由，此处配置项目路由
│   ├── services/          # 服务（统一管理 XHR 请求）
│   ├── utils/             # 工具类
│   ├── views/             # 路由页面组件
│   ├── App.vue             # 根组件
│   ├── main.js             # 入口文件
├── index.html         # 主页，打开网页后最先访问的页面
├── static/              # 放置无需经由 Webpack 处理的静态文件，通常放置图片类资源
├── .babelrc             # Babel 转码配置
├── .editorconfig             # 代码格式
├── .eslintignore        # （配置）ESLint 检查中需忽略的文件（夹）
├── .eslintrc            # ESLint 配置
├── .gitignore           # （配置）在上传中需被 Git 忽略的文件（夹）
├── package.json         # 本项目的配置信息，启动方式
├── package-lock.json         # 记录当前状态下实际安装的各个npm package的具体来源和版本号
├── README.md         # 项目说明（很重要，便于其他人看懂）
```

Some resources I got inspired by

[vuex所展示的目录结构](https://vuex.vuejs.org/en/structure.html)

[Even实例项目](https://github.com/vuejs/vue-hackernews-2.0/tree/master/src)

[博客详解](https://www.cnblogs.com/chenleideblog/p/10432375.html)

