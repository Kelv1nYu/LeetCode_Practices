**704. [Binary_Search.py](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Binary_Search.py)**      Level: Easy

中文：
* 定义 target 是在一个在左闭右闭的区间里，也就是`[left, right]`。
    * `while (left <= right)` 要使用 `<=` ，因为`left == right`是有意义的，所以使用 `<=`。
    * `if (nums[middle] > target)` `right` 要赋值为 `middle - 1`，因为当前这个`nums[middle]`一定不是`target`，那么接下来要查找的左区间结束下标位置就是 `middle - 1`。

English:

* The definition target is in an interval that is closed on the left and closed on the right, which is `[left, right]`.
     * `While (left <= right)` to use `<=`, because `left == right` is meaningful, so use `<=`.
     * `if (nums[middle]> target)` `right` should be assigned `middle-1`, because the current `nums[middle]` must not be the `target`, then the end subscript position of the left interval to be searched next is `middle-1`.