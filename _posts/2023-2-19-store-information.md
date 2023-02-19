# 存储信息

## 问题

因为 HTTP 协议是无状态的，即服务器不知道用户上一次做了什么。

当多个客户端访问服务器时会发送多个Http请求。如果不对Http请求进行处理，则无法得知Http请求具体来自哪个客户端。

现在，设想下面场景：

1. 两个社畜在两台电脑上登录自己的账号
2. 两个社畜分别修改用户信息

上述简单来说执行了四个Http请求，两个登陆请求，两个修改用户信息的请求。如果不对Http做标记，这四个请求对与服务器来说只能根据URL地址来判断出这是两个业务需求，分别是登陆功能需求和修改用户信息功能需求。这将导致服务器无法得知修改用户信息请求来自于哪个客户端，从而无法判断这个客户端是否登陆用户及登陆的用户是哪个，最终导致无法修改用户信息。

## 解决方案

为每个用户创建不同的会话，给Http请求添加会话相关联的信息，这样用户的每次请求都只会在指定的会话中进行。

具体步骤：

1. 客户端Http请求，该请求涉及会话，
2. 服务器根据请求中cookie是否含有sessionid来判断，有则找到指定session进行操作，否则创建一个新会话并在响应中加入`Set-Cookie=<sessionid>; Path=/; HttpOnly`来创建cookie。

会话起到什么作用？

Session是一种服务器端的机制，Session 对象用来存储特定用户会话所需的信息，比如存储你的登陆状态等。Session由服务端生成，保存在服务器的内存、缓存、硬盘或数据库中。

现在问题来了，如何把会话编号加入到http请求中呢？

这需要使用到cookie，cookie内容时键值对形式的，cookie会和服务器地址绑定。当向cookie绑定的服务器地址发送请求时，所有http请求会添加上cookie的键值对，然后服务器就根据sessionid找到之前的session，从上次session的操作继续执行。

cookie也分为两种，内存cookie和硬盘cookie，内存cookie会随着浏览器的关闭而消失，这也是为什么在某网页登陆用户后浏览器未关闭，再访问该网页仍需要登陆的原因。而大多使用硬盘cookie，所以只要cookie不删除，你的用户登陆会一直存在。

cookies跨域写入失败

当后端项目向浏览器写入cookies时，后端项目协议、域名、端口必须相同时才能写到浏览器.。
比如我访问一个地址为 http://test.clock.bone:8080 的页面地址，这个页面地址 请求一个后端服务如：http://test.clock.bone:8080/getinfo ,这个接口向浏览器写入了cookie 。 只有当浏览器地址和协议、域名、端口和请求的后端服务的协议、域名、端口一致时，这个cookie才能写成功，即使其它都 一样 ，但端口不一样也不会成功。
所以如果 浏览器访问的是 http://test.clock.bone:8080，这个页面请求了后端服务http://test.clock.bone:8081/getinfo 写入了cookies也不会成功的原因。

session跨域每次获取sessionid不一样

我们知道session也依赖于cookie，当服务端创建了sessionid 要写入浏览器cookies时，如果不同源，那么sessionid会写入失败，下次请求时 浏览器无法携带session，服务端没有获取到sessionid ，于是又会重新创建一个sessionId，这就是为什么跨域请求 每次得到的sessionid不一致的原因。

session创建时间

session在访问tomcat服务器HttpServletRequest的getSession(true)的时候创建，tomcat的ManagerBase类提供创建sessionid的方法：随机数+时间+jvmid