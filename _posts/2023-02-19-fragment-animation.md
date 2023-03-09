```xml
<fragment ...>
  <action
					...
          app:popEnterAnim="@anim/slide_in_left"
          app:popExitAnim="@anim/slide_out_right"
          app:enterAnim="@anim/slide_in_right"
          app:exitAnim="@anim/slide_out_left"/>
</fragment>
```

`Back`会触发 `popEnterAnim`和`popExitAnim`，比如当前处于`fragmentB`，点击`Back`退出到`fragmentA`，那么就会触发`fragmentsB`的`popExitAnim`，以及`fragmentA`的`popExitAnim`，`pop`可以理解为栈的弹出。

非`Back`会触发`enterAnim`和`exitAnim`，比如当前`fragmentA`，点击当前界面的按钮会导航到`fragmentB`，那么就会触发`fragmentA`的`exitAnim`，以及`fragmentB`的`enterAnim`。

