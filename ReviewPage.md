# Review Page

本页面为所有代码的做法与总结。

---
**0. [Two_Sum.py](https://github.com/Kelv1nYu/leetCode_practices/blob/master/Code/Two_Sum.py)**      Level: Easy
      

1. 将target与num的差值作为key，nums的index作为值存入字典，通过index遍历nums列表，同时比对字典的keys，若比对成功，返回两个index；失败则进行下一个值的比对。
2. 不足与失误：
   1. 思维不够灵活、发散：开始没有想到通过字典的key-valuet特性进行差值与index的关联；
   2. 考虑问题不够全面：没有考虑到各种情况，例如两个相同的列表元素相加等于target等等；
   3. 返回值设定问题：由于只用返回一个两个元素的列表即可，所以在比对成功之后直接返回[a,b]即可，使用新建一个列表并在比对成功后将两个index依次append进去的方法耗时更长一些。


---
**1. [Jewels_and_Stones.py](https://github.com/Kelv1nYu/leetCode_practices/blob/master/Code/Jewels_and_Stones.py)**      Level: Easy
      

1. 遍历S字符串同时与J字符串进行比对。
2. 优化：


---
**2. [Hamming_Distance.py](https://github.com/Kelv1nYu/leetCode_practices/blob/master/Code/Hamming_Distance.py)**      Level: Easy
      

1. 将整形转化为二进制字符串，逐一比对。
2. 不足与失误：
   1. 如直接用内置函数bin()进行转换会生成'0b'开头的字符串，故使用str.format()方法['{0:b}'.format()]来将十进制整形转换为二进制字符串。
3. 另一种做法<code>bin(x^y).count(1)</code>,即直接使用亦或运算，转化为二进制之后再用str.count()方法计算1出现的次数。（该方法虽只需一行，但运行所需时间比我的方法要长，故不清楚是否算优化）


---
**3. [Judge_Route_Circle.py](https://github.com/Kelv1nYu/leetCode_practices/blob/master/Code/Judge_Route_Circle.py)**      Level: Easy
      

1. 新建一个元组（x, y）作为原点，遍历字符串，根据UDLF进行x、y的加减操作，最后判断x，y是否皆为0。
2. 不足与失误：
   1. 可以直接使用str.count()函数判断字符串内的UDLF数量，通过判断U与D，L与F的数量是否相等来返回True或False；
   2. 缩写为一行代码即 <code>return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")</code>；
   3. 该代码运行所需时间较少。


---
**4. [Self_Dividing_Numbers.py](https://github.com/Kelv1nYu/leetCode_practices/blob/master/Code/Self_Dividing_Numbers.py)**      Level: Easy
      

1. 将int类型转换为str类型，对其中每一个数字取余；判断余数为0的次数是否等于数字位数，添加到list中或跳过该数字。
2. 将范围内所有符合条件的数字放到list中，只需判断input的数字是否在该list中即可。（虽耗时少，但不推荐）
3. 运算符<code>//</code>为取整除 - 返回商的整数部分。
4. 返回值书写方式：
   1. [对(x)的操作 for x in 集合 if 条件]
   2. [对(x,y)的操作 for x in 集合1 for y in 集合2 if 条件]


---
**5. [Array_Partition_I.py](https://github.com/Kelv1nYu/leetCode_practices/blob/master/Code/Array_Partition_I.py)**      Level: Easy
      

1. 使用list的sort函数将其进行排序。
2. 由于顺序已经排好，所以将list中的元素两两分组取最小值时，最小值必定为前一个数字。所以将该list进行step为2的切片得到一个新的数组并对内部元素求和即可。
3. 求和时可以选用for循环进行累加，也可以使用python3内置的sum()函数。


---
**6. [Number_Complement.py](https://github.com/Kelv1nYu/leetCode_practices/blob/master/Code/Number_Complement.py)**      Level: Easy
      

1. 通过str.format()进行进制转换。
2. 按位取反操作既可以使用等长的全为1的int类型与转换后的int(num)做减法，也可以做亦或。
3. 另附一种一行代码：<code>return ~(-1 << num.bit_length()) & ~num</code>(bit_length返回表示该数字的时占用的最少位数)由于<code>~</code>操作符会将符号位一并取反，所以通过bit_length()方法获得除去符号位的位数，通过与左移该位数的-1(二进制表示为11，取反后表示为00)进行<code>&</code>操作，得到去掉符号位的<code>~num</code>。


---