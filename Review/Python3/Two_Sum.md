**1. [Two_Sum.py](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Two_Sum.py)**      Level: Easy
      

中文：
* 顺序扫描数组，对每一个元素，在 map 中找能组合给定值的另一半数字，如果找到了，直接返回两个数字的下标即可。如果找不到，就把这个数字存入 map 中，等待扫到“另一半”数字的时候，再取出来返回结果。

English: 
* Scan the array in order, for each element, find the "other half" of the number in the map that can combine the given value, and if it exists, return the index of the two numbers directly. Or, store this number in the map, wait for the "other half" of the number to be scanned, and then take it out to return the result.