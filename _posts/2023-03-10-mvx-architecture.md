# Architecture

MVC MVP MVVM

前面的 MV分别代表者 Model（数据来源，可以使类或者数据库等）以及View（视图）

MVC中的Controller控制器负责处理视图和模型之间的交互，同时也负责处理其他方面的逻辑，例如路由、认证等。

MVP中的Presenter只负责处理视图和模型之间的交互。

*MVC和MVP关系比较暧昧，MVP中的P理论上是这么做，但实际上如果需要也会充当Controller的角色*

MVVM中的ViewModel是连接着View和Model的桥梁，当Model改变是会通知到View。

