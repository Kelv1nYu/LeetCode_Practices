**215. [Kth_Largest_Element_in_an_Array.py](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Kth_Largest_Element_in_an_Array.py)**      Level: Medium

中文：
* 最简单的办法是将数组排序并倒序取出第k大的数， 时间复杂度为O(nlogn)；
* 或者可以使用快排的思想，但经过判断后只对其中一侧继续进行分区，最终得到第k大的数字。平均时间复杂度为O(n)，最差时间复杂度为O(n<sup>2</sup>)。

English:

* The easiest way is to sort the array and take out the k-th largest number in reverse order. The time complexity is O(nlogn);
* Or you can use the idea of fast sorting, but after checking pivot index, only one side of the partition is continued, and the k-th largest number is finally found. The average time complexity is O(n), and the worst time complexity is O(n<sup>2</sup>).