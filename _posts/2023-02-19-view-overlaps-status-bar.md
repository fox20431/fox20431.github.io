视图与状态栏重叠

原因：

状态栏设置透明。

解决方案：

1. 自动适配窗口大小

Use `android:fitsSystemWindows="true"` in the root view of your layout (LinearLayout in your case). And `android:fitsSystemWindows` is an 

> internal attribute to adjust view layout based on system windows such as the status bar. If true, adjusts the padding of this view to leave space for the system windows. Will only take effect if this view is in a non-embedded activity.
>
> Must be a boolean value, either "true" or "false".
>
> This may also be a reference to a resource (in the form "@[package:]type:name") or theme attribute (in the form "?[package:][type:]name") containing a value of this type.
>
> This corresponds to the global attribute resource symbol fitsSystemWindows.

原文链接：https://stackoverflow.com/questions/29738510/toolbar-overlapping-below-status-bar

2. 获取状态栏高度填充