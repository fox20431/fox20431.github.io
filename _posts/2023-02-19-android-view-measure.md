# Android View Measure



## Measure Specification

Android引入测量规格（Measure Specification）概念，并为其在View中创建了MeasureSpec静态内部类，让我们去看看这个静态内部类。

```java
public static class MeasureSpec {

    private static final int MODE_SHIFT = 30;
    private static final int MODE_MASK  = 0x3 << MODE_SHIFT;

    /** @hide */
    @IntDef({UNSPECIFIED, EXACTLY, AT_MOST})
    @Retention(RetentionPolicy.SOURCE)
    public @interface MeasureSpecMode {}

    /**
     * Measure specification mode: The parent has not imposed any constraint
     * on the child. It can be whatever size it wants.
     */
    public static final int UNSPECIFIED = 0 << MODE_SHIFT;

    /**
         * Measure specification mode: The parent has determined an exact size
         * for the child. The child is going to be given those bounds regardless
         * of how big it wants to be.
         */
    public static final int EXACTLY     = 1 << MODE_SHIFT;

    /**
         * Measure specification mode: The child can be as large as it wants up
         * to the specified size.
         */
    public static final int AT_MOST     = 2 << MODE_SHIFT;

    /**
         * Creates a measure specification based on the supplied size and mode.
         *
         * The mode must always be one of the following:
         * <ul>
         *  <li>{@link android.view.View.MeasureSpec#UNSPECIFIED}</li>
         *  <li>{@link android.view.View.MeasureSpec#EXACTLY}</li>
         *  <li>{@link android.view.View.MeasureSpec#AT_MOST}</li>
         * </ul>
         *
         * <p><strong>Note:</strong> On API level 17 and lower, makeMeasureSpec's
         * implementation was such that the order of arguments did not matter
         * and overflow in either value could impact the resulting MeasureSpec.
         * {@link android.widget.RelativeLayout} was affected by this bug.
         * Apps targeting API levels greater than 17 will get the fixed, more strict
         * behavior.</p>
         *
         * @param size the size of the measure specification
         * @param mode the mode of the measure specification
         * @return the measure specification based on size and mode
         */
    public static int makeMeasureSpec(@IntRange(from = 0, to = (1 << MeasureSpec.MODE_SHIFT) - 1) int size,
                                      @MeasureSpecMode int mode) {
        // ...
    }

    /**
         * Like {@link #makeMeasureSpec(int, int)}, but any spec with a mode of UNSPECIFIED
         * will automatically get a size of 0. Older apps expect this.
         *
         * @hide internal use only for compatibility with system widgets and older apps
         */
    @UnsupportedAppUsage
    public static int makeSafeMeasureSpec(int size, int mode) {
        // ...
    }

    /**
         * Extracts the mode from the supplied measure specification.
         *
         * @param measureSpec the measure specification to extract the mode from
         * @return {@link android.view.View.MeasureSpec#UNSPECIFIED},
         *         {@link android.view.View.MeasureSpec#AT_MOST} or
         *         {@link android.view.View.MeasureSpec#EXACTLY}
         */
    @MeasureSpecMode
    public static int getMode(int measureSpec) {
        // ...
    }

    /**
         * Extracts the size from the supplied measure specification.
         *
         * @param measureSpec the measure specification to extract the size from
         * @return the size in pixels defined in the supplied measure specification
         */
    public static int getSize(int measureSpec) {
        // ...
    }

    /**
         * Returns a String representation of the specified measure
         * specification.
         *
         * @param measureSpec the measure specification to convert to a String
         * @return a String with the following format: "MeasureSpec: MODE SIZE"
         */
    static int adjust(int measureSpec, int delta) {
        // ...
    }
    public static String toString(int measureSpec) {
        // ...
    }
}
```



- UNSPECIFIED模式：本质就是不限制模式，父视图不对子View进行任何约束，View想要多大要多大，想要多长要多长;
- EXACTLY模式：该模式其实对应的场景就是match_parent或者是一个具体的数据(50dp或80px)，父视图为子View指定一个确切的大小，无论子View的值设置多大，都不能超出父视图的范围;
- AT_MOST模式：这个模式对应的场景就是wrap_content，其内容就是父视图给子View设置一个最大尺寸，子View只要不超过这个尺寸即可;