list 不能在遍历的时候更新
```kotlin
for (str in list) {
    if (someCondition) {
        myArrayList.removeAt(str);
    }
}
```