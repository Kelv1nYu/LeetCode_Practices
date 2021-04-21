**540. [Single_Element_in_a_Sorted_Array.py](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Single_Element_in_a_Sorted_Array.py)**      Level: Medium

中文：
* 使用二分搜索, 在移动边界值的时候分情况讨论（该数组为有序数组且只存在一个唯一值，所以一定有奇数个数字，只需经两次判断找到奇数个数字的部分即可继续搜索）：
    * 若当前中值与右侧值相等：
        * 判断当前中值左右两边的值的数量是否为偶数，若是，则唯一值在右侧，将左边界右移；若否，则唯一值在左侧，将右边界左移。
    * 若当前中值与左侧值相等：
        * 判断当前中值左右两边的值的数量是否为偶数，若是，则唯一值在左侧，将右边界左移；若否，则唯一值在右侧，将左边界右移。

English:

* Use binary search to discuss the situation when moving the boundary value (The array is an ordered array and only contains one unique value, so there must be an odd number of numbers. After judgment, the part with odd numbers is the part where the unique value is located):
    * If the current median value is equal to the right value:
        * Determine whether the number of values on the left and right sides of the current median is even. If so, the unique value is on the right, and the left boundary is shifted to the right; if not, the unique value is on the left, and the right boundary is shifted to the left.
    * If the current median value is equal to the left value:
        * Determine whether the number of values on the left and right sides of the current median is even. If so, the unique value is on the left, and the right boundary is shifted to the left; if not, the unique value is on the right, and the left boundary is shifted to the right.
