# credential

在`main.ts`设置全局属性：

前端每次请求携带credential：

```js
axios.defaults.withCredentials=true;
```

其实就是每次请求发送包含相同session的cookie，请求头会添加下面内容：

```http
Cookie:JSESSIONID=your session id
```

后端允许前端携带credential：

```java
@CrossOrigin(origins = "http://localhost:3000", allowCredentials = "true")
```

`origins`允许跨域的地址，默认在响应头添加：

```http
Access-Control-Allow-Origin: http://localhost:3000
```

`allowCredential`是否允许携带凭证，默认在响应头添加：

```http
Access-Control-Allow-Credentials: true
```

`allowCredential`默认为字符串`false`，如果不设置为`true`，前端即使携带了`credential`也无法使用。