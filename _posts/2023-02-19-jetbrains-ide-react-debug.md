在Jetbrains的IDE上进行debug

run -> edit configurations -> + -> java script debug

url填写自己的地址

在源码地方src填写remote URL 为 webpack:///src



这样run任务里就有你自定义的任务，但是该任务只能使用debug，但debug之前需要你项目线运行起来，这样debug才能定位到你的资源。