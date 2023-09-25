# Tailwind

通过约定的名称来指代样式，可以省去大量的代码以及切换标签的烦恼。

## Documentation

如果查看类型指代何种样式？

https://tailwindcss.com/docs/

通过官方网站可以查看你想要的样式。

## THERE BE DRAGON

比较坑的是，tailwind会有一些默认的样式，比如`font-size`，这些样式会覆盖掉你自己的样式，所以你需要在`tailwind.config.js`中进行配置。

比如他会有默认outline之类的。