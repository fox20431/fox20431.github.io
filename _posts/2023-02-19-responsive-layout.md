# 响应式布局

## 条件

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

## 使用

### link中使用@media：

```html
<link rel=“stylesheet” type=“text/css” media=“only screen and （max-width： 480px），only screen and （max-device-width： 480px）” href=“link.css”/>
```

### 在样式表中内嵌@media：

```css
@media ( min-device-width:1024px ) and ( max-width:989px )，screen and ( max-device-width:480px )，( max-device-width:480px ) and ( orientation:landscape )，( min-device-width:480px ) and ( max-device-width:1024px ) and ( orientation:portrait ) {srules}
```