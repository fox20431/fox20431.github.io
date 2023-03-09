---
title: "排序算法"
excerpt: "记录常见的排序算法"
---

# Sort Algorithm


冒泡排序：

```java
public class BubbleSort {
    public static void main(String[] args) {
        // the array to be sorted
        int[] arr = {4, 3, 5, 7, 9, 6};
        for (int i = 0; i < arr.length - 1; i++ ) { // every time this loop is executed, a maximum value will be selected, the last value is naturally correct
            // whether it is ordered, ordered by default, disordered when exchange occurs
            boolean ordered = true;
            for (int j = 0; j < arr.length - i - 1; j++) {
                if (arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    ordered = false;
                }
            }
            if (ordered) {
                break;
            }
        }
        System.out.println(Arrays.toString(arr));
    }
}
```


选择排序：

```java
public class SelectionSort {
    public static void main(String[] args) {
        int[] arr = {3, 9, -1, 10, -2};
        for (int i = 0; i < arr.length -1; i++) {
            // assuming the current number is the minimum value
            int min = arr[i];
            int minIndex = i;
            for (int j = i+1; j < arr.length; j++) { // select the minimum number
                if (min > arr[j]) {
                    min = arr[j];
                    minIndex = j;
                }
            }
            arr[minIndex] = arr[i];
            arr[i] = min;
        }
        System.out.println(Arrays.toString(arr));
    }
}
```


插入排序：

```java
public class InsertionSort {
    public static void main(String[] args) {
        int[] arr = {4, 1, 9, 2, 5};
        // 从第二个元素开始，默认第一个元素有序
        for (int i = 1; i < arr.length; i++ ){
            // 记录要插入的元素
            int temp = arr[i];
            int j = i;
            while (j > 0 && arr[j-1] > temp) {
                arr[j] = arr[j-1]; // 值在数组顺序中右移，为插入的位置留出空间
                j--;
            }
            arr[j] = temp;
        }
        System.out.println(Arrays.toString(arr));
    }
}
```

堆排序：

```java
public class HeapSort {
    public static void heapSort(int[] arr) {
        int n = arr.length;

        // build heap
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(arr, n, i);

        // extract elements from heap one by one
        for (int i = n - 1; i >= 0; i--) {
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            // call heapify on the reduced heap
            heapify(arr, i, 0);
        }
    }

    public static void heapify(int[] arr, int n, int i) {
        int largest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;

        if (l < n && arr[l] > arr[largest])
            largest = l;

        if (r < n && arr[r] > arr[largest])
            largest = r;

        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;

            // recursively heapify the affected sub-tree
            heapify(arr, n, largest);
        }
    }

    public static void main(String[] args) {
        int[] arr = { 9, 4, 2, 6, 3 };
        heapSort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
```