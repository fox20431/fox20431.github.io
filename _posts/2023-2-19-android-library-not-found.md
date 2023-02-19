最近从GitHub上下载了Android Developer官方的example，准备看看如何实现的，但是遇到了问题。

```kotlin
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.TextView
```

上述代码提示`android.xxx`无法解析

解决方案，`app/build.gradle`更改`targetSdkVersion <android version>`即可解决方案，其原因应该是你本地的SDK与对应版本不一致导致找不到对应的库。

