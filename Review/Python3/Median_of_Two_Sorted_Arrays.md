**4. [Median_of_Two_Sorted_Arrays.py](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Median_of_Two_Sorted_Arrays.py)**      Level: Hard
      

中文：
* 先二分产生一个 midA 和 mid B 并使线左边的数都小于右边的数：即，nums1[midA-1] ≤ nums2[midB] && nums2[midB-1] ≤ nums1[midA] 。
* 如果不满足上述条件，切分线就需要移动：
    * 如果 nums1[midA] < nums2[midB-1]，说明 midA 这条线划分出来左边的数小了，切分线应该右移；
    * 如果 nums1[midA-1] > nums2[midB]，说明 midA 这条线划分出来左边的数大了，切分线应该左移。经过多次调整以后，切分线总能找到满足条件的解。

* 找到两条切分线之后，数组 1 在切分线两边的下标分别是 midA - 1 和 midA。数组 2 在切分线两边的下标分别是 midB - 1 和 midB。
* 合并成最终数组：
    * 如果数组长度是奇数，那么中位数就是 max(nums1[midA-1], nums2[midB-1]；
    * 如果数组长度是偶数，那么中间位置的两个数依次是：max(nums1[midA-1], nums2[midB-1]) 和 min(nums1[midA], nums2[midB])，那么中位数就是 (max(nums1[midA-1], nums2[midB-1]) + min(nums1[midA], nums2[midB])) / 2。

English: 
* First set mid line A and mid line B to make the numbers on the left side of the lines are less than the numbers on the right side: that is, nums1[midA-1] ≤ nums2[midB] && nums2[midB-1] ≤ nums1[midA]. 
* If these conditions are not met, the cutting line needs to be adjusted:
    * If nums1[midA] < nums2[midB-1], it means that the number on the left of the line dividing midA is small, and the dividing line should be shifted to the right; 
    * If nums1[midA-1]> nums2[midB], it means midA The number on the left side of the line division is larger, and the division line should be shifted to the left.

* After finding the two mid lines, the subscripts of array 1 on both sides of the cutting line are midA-1 and midA. The subscripts of array 2 on both sides of the cutting line are midB-1 and midB. 
* Merge 2 arrays into the final array:
    * If the length of the array is odd, then the median is max(nums1[midA-1], nums2[midB-1]);
    * If the array length is even, then the two numbers in the middle position are in order: max(nums1[midA-1], nums2[midB-1]) and min(nums1[midA], nums2[midB]), then the median It is (max(nums1[midA-1], nums2[midB-1]) + min(nums1[midA], nums2[midB])) / 2.