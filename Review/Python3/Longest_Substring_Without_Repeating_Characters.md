**3. [Longest_Substring_Without_Repeating_Characters.py](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Longest_Substring_Without_Repeating_Characters.py)**      Level: Medium
      

中文：
* 滑动窗口的右边界不断的右移，只要没有重复的字符，就持续向右扩大窗口边界。一旦出现了重复字符，就需要缩小左边界，直到重复的字符移出了左边界，然后继续移动滑动窗口的右边界。以此类推，每次移动需要计算当前长度，并判断是否需要更新最大长度，最终最大的值就是题目中的所求。

English: 
* The right border of the sliding window keeps expanding to the right as long as there are no repeated characters. Once the repeated characters appear, the left border needs to move until the repeated characters move out of the left border, and then continue to move the right border of the sliding window. By analogy, each movement needs to calculate the current length, and determine whether the maximum length needs to be updated, and the final maximum value is what is required in the question.