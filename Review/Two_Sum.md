**0. [Two_Sum.py](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Two_Sum.py)**      Level: Easy
      

1. 将target与num的差值作为key，nums的index作为值存入字典，通过index遍历nums列表，同时比对字典的keys，若比对成功，返回两个index；失败则进行下一个值的比对。
2. 不足与失误：
   1. 思维不够灵活、发散：开始没有想到通过字典的key-valuet特性进行差值与index的关联；
   2. 考虑问题不够全面：没有考虑到各种情况，例如两个相同的列表元素相加等于target等等；
   3. 返回值设定问题：由于只用返回一个两个元素的列表即可，所以在比对成功之后直接返回[a,b]即可，使用新建一个列表并在比对成功后将两个index依次append进去的方法耗时更长一些。