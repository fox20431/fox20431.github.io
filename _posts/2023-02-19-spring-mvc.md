# Spring MVC

前端如果传过来的是json格式的字符串，后台参数需要加@RequestBody注解，这个注解表示的是一个对象，不能指定字段。

@RequestPart

For access to a part in a `multipart/form-data` request, converting the part’s body with an `HttpMessageConverter`. See [Multipart](https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-multipart-forms).

方法的所有参数：

具体可见：https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-ann-arguments

---

Spring REST - binding GET parameters to nested objects

https://stackoverflow.com/questions/36650051/spring-rest-binding-get-parameters-to-nested-objects

---



pageable 传递参数localhost:8091/endpoint/test?page=0&size=3&sort=id,DESC