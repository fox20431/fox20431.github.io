| 状态码 | 事件                                       | 意义|
| ------ | ------------------------------------------ | :-- |
| 1xx   | Informational | 代表请求已被接受，需要继续处理。 |
| 2xx    | Success |代表请求已成功被服务器接收、理解、并接受。|
| 3xx | Redirection |代表需要客户端采取进一步的操作才能完成请求。|
| 4xx | Client Error |代表了客户端看起来可能发生了错误，妨碍了服务器的处理。|
| 5xx | Server Error  |表示服务器无法完成明显有效的请求。|

100 Continue
101 Switching protocols

200 OK
201 Created
202 Accepted
203 Non-Authoritative Information
204 No Content
205 Reset Content
206 Partial Content

300 Multiple Choices
301 Moved Permanently
302 Found
303 See Other
304 Not Modified
305 Use Proxy
307 Temporary Redirect

400 Bad Request
401 Unauthorized
402 Payment Required
403 Forbidden
404 Not Found
405 Method Not Allowed
406 Not Acceptable
407 Proxy Authentication Required
408 Request Timeout
409 Conflict
410 Gone
411 Length Required
412 Precondition Failed
413 Request Entity Too Large
414 Request-URI Too Long
415 Unsupported Media Type
416 Requested Range Not Suitable
417 Expectation Failed

500 Internal Server Error
501 Not Implemented
502 Bad Gateway
503 Service Unavailable
504 Gateway Timeout
505 HTTP Version Not Supported

[readyState](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/readyState)

0 (未初始化) 对象已建立，但是尚未初始化（尚未调用open方法）
1 (初始化) 对象已建立，尚未调用send方法
2 (发送数据) send方法已调用，但是当前的状态及http头未知
3 (数据传送中) 已接收部分数据，因为响应及http头不全，这时通过responseBody和responseText获取部分数据会出现错误，
4 (完成) 数据接收完毕,此时可以通过通过responseBody和responseText获取完整的回应数据