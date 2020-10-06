# Review Page

本页面为所有代码的做法与总结。


**1. [Jewels_and_Stones.py](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Jewels_and_Stones.py)**      Level: Easy
      

1. 遍历S字符串同时与J字符串进行比对。
2. 优化：


---
**2. [Hamming_Distance.py](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Hamming_Distance.py)**      Level: Easy
      

1. 将整形转化为二进制字符串，逐一比对。
2. 不足与失误：
   1. 如直接用内置函数bin()进行转换会生成'0b'开头的字符串，故使用str.format()方法['{0:b}'.format()]来将十进制整形转换为二进制字符串。
3. 另一种做法<code>bin(x^y).count(1)</code>,即直接使用亦或运算，转化为二进制之后再用str.count()方法计算1出现的次数。（该方法虽只需一行，但运行所需时间比我的方法要长，故不清楚是否算优化）


---
**3. [Judge_Route_Circle.py](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Judge_Route_Circle.py)**      Level: Easy
      

1. 新建一个元组（x, y）作为原点，遍历字符串，根据UDLF进行x、y的加减操作，最后判断x，y是否皆为0。
2. 不足与失误：
   1. 可以直接使用str.count()函数判断字符串内的UDLF数量，通过判断U与D，L与F的数量是否相等来返回True或False；
   2. 缩写为一行代码即 <code>return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")</code>；
   3. 该代码运行所需时间较少。


---
**4. [Self_Dividing_Numbers.py](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Self_Dividing_Numbers.py)**      Level: Easy
      

1. 将int类型转换为str类型，对其中每一个数字取余；判断余数为0的次数是否等于数字位数，添加到list中或跳过该数字。
2. 将范围内所有符合条件的数字放到list中，只需判断input的数字是否在该list中即可。（虽耗时少，但不推荐）
3. 运算符<code>//</code>为取整除 - 返回商的整数部分。
4. 返回值书写方式：
   1. [对(x)的操作 for x in 集合 if 条件]
   2. [对(x,y)的操作 for x in 集合1 for y in 集合2 if 条件]


---
**5. [Array_Partition_I.py](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Array_Partition_I.py)**      Level: Easy
      

1. 使用list的sort函数将其进行排序。
2. 由于顺序已经排好，所以将list中的元素两两分组取最小值时，最小值必定为前一个数字。所以将该list进行step为2的切片得到一个新的数组并对内部元素求和即可。
3. 求和时可以选用for循环进行累加，也可以使用python3内置的sum()函数。


---
**6. [Number_Complement.py](https://github.com/Kelv1nYu/leetCode_practices/blob/master/Code/Number_Complement.py)**      Level: Easy
      

1. 通过str.format()进行进制转换。
2. 按位取反操作既可以使用等长的全为1的int类型与转换后的int(num)做减法，也可以做亦或。
3. 另附一种一行代码：<code>return ~(-1 << num.bit_length()) & ~num</code>(bit_length返回表示该数字的时占用的最少位数)由于<code>~</code>操作符会将符号位一并取反，所以通过bit_length()方法获得除去符号位的位数，通过与左移该位数的-1(二进制表示为11，取反后表示为00)进行<code>&</code>操作，得到去掉符号位的<code>~num</code>。


---
**7. [Reverse_String.py](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Reverse_String.py)**      Level: Easy
      

1. 使用切片（Slice）直接返回从后至前排列的字符串。


---
**8. [Reverse_Words_in_a_String_III.py](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Reverse_Words_in_a_String_III.py)**      Level: Easy
      

1. 使用split()方法将字符串用空格隔开，遍历得到的字符串列表，使用字符串加法将反向排序的字符串（使用切片实现反向排序）相加，去掉首尾的空格
2. join()方法可以将序列中的元素以指定的字符连接生成一个新的字符串。
3. 另附两个第二种方法的代码：
   1. <code>words = s.split(' ')</code><br>
      <code>return ' '.join([x[::-1] for x in words])</code>
   2. <code>return ' '.join(s.split()[::-1])[::-1]</code>


---
**9. [Defanging_an_IP_Address.py](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Defanging_an_IP_Address.py)**      Level: Easy
      

1. 使用split()方法将字符串用 "." 隔开，遍历得到的字符串列表，使用字符串加法将字符串与 "[.]" 相连。


---




| Squence | Problem       | Level  | Language  | Tags |
|:-------:|:--------------|:------:|:---------:|:----:|
|1|[Two_Sum](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Two_Sum.md)|Easy|Python3|[Array]|
|2|[Add_Two_Numbers](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Add_Two_Numbers.md)|Medium|Python3|[Linked List]|
|14|[Longest_Common_Prefix](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Longest_Common_Prefix.md)|Easy|Python3|[String]|
|15|[3Sum](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/3Sum.md)|Medium|Python3|[Array]
|19|[Remove_Nth_Node_From_End_of_List](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Remove_Nth_Node_From_End_of_List.md)|Medium|Python3|[Linked List]|
|21|[Merge_Two_Sorted_Lists](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Merge_Two_Sorted_Lists.md)|Easy|Python3|[Linked List]|
|24|[Swap_Nodes_in_Pairs](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Swap_Nodes_in_Pairs.md)|Medium|Python3|[Recursion]|
|26|[Remove_Duplicates_from_Sorted_Array](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Remove_Duplicates_from_Sorted_Array.md)|Easy|Python3|[Array]|
|27|[Remove_Element](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Remove_Element.md)|Easy|Python3|[Array]|
|28|[Implement_strStr()](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Implement_strStr.md)|Easy|Python3|[String]|
|50|[Pow(x, n)](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Pow_x_n.md)|Medium|Python3|[Recursion]
|54|[Spiral_Matrix](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Spiral_Matrix.md)|Medium|Python3|[Matrix]|
|61|[Rotate_List](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Rotate_List.md)|Medium|Python3|[Linked List]|
|66|[Plus_One](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Plus_One.md)|Easy|Python3|[Array]|
|67|[Add_Binary](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Add_Binary.md)|Easy|Python3|[String]|
|70|[Climbing_Stairs](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Climbing_Stairs.md)|Easy|Python3|[Recursion]
|78|[Subsets](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Subsets.md)|Medium|Python3|[Array]
|79|[Word_Search](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Word_Search.md)|Medium|Python3|[Tree]
|88|[Merge_Sorted_Array](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Merge_Sorted_Array.md)|Easy|Python3|[Array]|
|95|[Unique_Binary_Search_Trees_II](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Unique_Binary_Search_Trees_II.md)|Medium|Python3|[Recursion]
|98|[Validate_Binary_Search_Tree](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Validate_Binary_Search_Tree.md)|Medium|Python3|[Tree]
|100|[Same_Tree](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Same_Tree.md)|Easy|Python3|[Tree]
|103|[Binary_Tree_Zigzag_Level_Order_Traversal](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Binary_Tree_Zigzag_Level_Order_Traversal.md)|Medium|Python3|[Tree]
|104|[Maximum_Depth_of_Binary_Tree](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Maximum_Depth_of_Binary_Tree.md)|Easy|Python3|[Recursion]
|106|[Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal.md)|Medium|Python3|[Tree]
|107|[Binary_Tree_Level_Order_Traversal_II](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Binary_Tree_Level_Order_Traversal_II.md)|Easy|Python3|[Tree]
|118|[Pascal's_Triangle](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Pascals_Triangle.md)|Easy|Python3|[Matrix]|
|119|[Pascal's_Triangle_II](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Pascals_Triangle_II.md)|Easy|Python3|[Matrix]|
|138|[Copy_List_with_Random_Pointer](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Copy_List_with_Random_Pointer.md)|Medium|Python3|[Linked List]|
|141|[Linked_List_Cycle](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Linked_List_Cycle.md)|Easy|Python3|[Linked List]|
|142|[Linked_List_Cycle_II](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Linked_List_Cycle_II.md)|Medium|Python3|[Linked List]|
|151|[Reverse_Words_in_a_String](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Reverse_Words_in_a_String.md)|Easy|Python3|[Array]|
|154|[Find_Minimum_in_Rotated_Sorted_Array_II](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Find_Minimum_in_Rotated_Sorted_Array_II.md)|Hard|Python3|[Array]
|160|[Intersection_of_Two_Linked_Lists](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Intersection_of_Two_Linked_Lists.md)|Easy|Python3|[Linked List]|
|167|[Two_Sum_II - Input_array_is_sorted](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Two_Sum_II_Input_array_is_sorted.md)|Easy|Python3|[Array]|
|173|[Binary_Search_Tree_Iterator](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Problems/Binary_Search_Tree_Iterator.md)|Medium|Python3|[Tree]|
|189|[Rotate_Array](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Rotate_Array.md)|Easy|Python3|[Array]|
|190|[Reverse_Bits](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Reverse_Bits.md)|Easy|Python3|[Bit Manipulation]
|203|[Remove_Linked_List_Elements](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Remove_Linked_List_Elements.md)|Easy|Python3|[Linked List]|
|206|[Reverse_Linked_List](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Reverse_Linked_List.md)|Easy|Python3|[Linked List]|
|209|[Minimum_Size_Subarray_Sum](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Minimum_Size_Subarray_Sum.md)|Medium|Python3|[Array]|
|210|[Course_Schedule_II](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Course_Schedule_II.md)|Medium|Python3|[Depth-first Search, Breadth-first Search]
|220|[Contains_Duplicate_III](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Problems/Contains_Duplicate_III.md)|Medium|Python3|[Tree]
|234|[Palindrome_Linked_List](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Palindrome_Linked_List.md)|Easy|Python3|[Linked List]|
|235|[Lowest_Common_Ancestor_of_a_Binary_Search_Tree](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Lowest_Common_Ancestor_of_a_Binary_Search_Tree.md)|Easy|Python3|[Tree]|
|258|[Add_Digits](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Add_Digits.md)|Easy|Python3|[Math]
|260|[Single_Number_III](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Single_Number_III.md)|Medium|Python3|[Bit Manipulation]
|264|[Ugly_Number_II](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Ugly_Number_II.md)|Medium|Python3|[Math]
|283|[Move_Zeroes](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Move_Zeroes.md)|Easy|Python3|[Array]|
|285|[Inorder_Successor_in_BST](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Inorder_Successor_in_BST.md)|Medium|Python3|[Tree]|
|328|[Odd_Even_Linked_List](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Odd_Even_Linked_List.md)|Medium|Python3|[Linked List]|
|344|[Reverse_String](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Reverse_String.md)|Easy|Python3|[String]|
|347|[Top_K_Frequent_Elements](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Top_K_Frequent_Elements.md)|Medium|Python3|[Hash Table]
|414|[Third_Maximum_Number](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Third_Maximum_Number.md)|Easy|Python3|[Array]|
|430|[Flatten_a_Multilevel_Doubly_Linked_List](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Flatten_a_Multilevel_Doubly_Linked_List.md)|Medium|Python3|[Linked List]|
|441|[Arranging_Coins](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Arranging_Coins.md)|Easy|Python3|[Binary Search, Math]
|448|[Find_All_Numbers_Disappeared_in_an_Array](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Find_All_Numbers_Disappeared_in_an_Array.md)|Easy|Python3|[Array]|
|450|[Delete_Node_in_a_BST](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Problems/Delete_Node_in_a_BST.md)|Medium|Python3|[Tree]|
|461|[Hamming_Distance](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Hamming_Distance.md)|Easy|Python3|[Bit Manipulation]|
|463|[Island_Perimeter](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Island_Perimeter.md)|Easy|Python3|[Hash Table]
|476|[Number_Complement](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Number_Complement.md)|Easy|Python3|[]|
|485|[Max_Consecutive_Ones](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Max_Consecutive_Ones.md)|Easy|Python3|[Array]|
|487|[Max_Consecutive_Ones_II](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Max_Consecutive_Ones_II.md)|Medium|Python3|[Array]|
|498|[Diagonal_Traverse](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Diagonal_Traverse.md)|Medium|Python3|[Matrix]|
|509|[Fibonacci_Number](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Fibonacci_Number.md)|Easy|Python3|[Recursion]|
|557|[Reverse_Words_in_a_String_III](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Reverse_Words_in_a_String_III.md)|Easy|Python3|[Array]|
|561|[Array_Partition_I](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Array_Partition_I.md)|Easy|Python3|[]|
|621|[Task_Scheduler](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Task_Scheduler.md)|Medium|Python3|[Math]
|657|[Robot_Return_to_Origin](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Judge_Route_Circle.md)|Easy|Python3|[]|
|662|[Maximum_Width_of_Binary_Tree](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Maximum_Width_of_Binary_Tree.md)|Medium|Python3|[Tree]
|700|[Search_in_a_Binary_Search_Tree](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Search_in_a_Binary_Search_Tree.md)|Easy|Python3|[Recursion]|
|701|[Insert_into_a_Binary_Search_Tree](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Problems/Insert_into_a_Binary_Search_Tree.md)|Medium|Python3|[Tree]|
|703|[Kth_Largest_Element_in_a_Stream](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Problems/Kth_Largest_Element_in_a_Stream.md)|Easy|Python3|[Tree]|
|707|[Design_Linked_List](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Design_Linked_List.md)|Medium|Python3|[Linked List]|
|708|[Insert_into_a_Sorted_Circular_Linked_List](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Insert_into_a_Sorted_Circular_Linked_List.md)|Medium|Python3|[Linked List]|
|724|[Find_Pivot_Index](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Find_Pivot_Index.md)|Easy|Python3|[Array]|
|728|[Self_Dividing_Numbers](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Self_Dividing_Numbers.md)|Easy|Python3|[]|
|747|[Largest_Number_At_Least_Twice_of_Others](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Largest_Number_At_Least_Twice_of_Others.md)|Easy|Python3|[Array]|
|771|[Jewels_and_Stones](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Jewels_and_Stones.md)|Easy|Python3|[HashTable]|
|779|[K-th_Symbol_in_Grammar](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/K_th_Symbol_in_Grammar.md)|Medium|Python3|[Recursion]
|797|[All_Paths_From_Source_to_Target](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/All_Paths_From_Source_to_Target.md)|Medium|Python3|[]
|905|[Sort_Array_By_Parity](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Sort_Array_By_Parity.md)|Easy|Python3|[Array]|
|941|[Valid_Mountain_Array](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Valid_Mountain_Array.md)|Easy|Python3|[Array]|
|957|[Prison_Cells_After_N_Days](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Prison_Cells_After_N_Days.md)|Medium|Python3|[Hash Table]
|977|[Squares_of_a_Sorted_Array](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Squares_of_a_Sorted_Array.md)|Easy|Python3|[Array]|
|1051|[Height_Checker](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Height_Checker.md)|Easy|Python3|[Array]|
|1089|[Duplicate_Zeros](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Duplicate_Zeros.md)|Easy|Python3|[Array]|
|1108|[Defanging_an_IP_Address](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Defanging_an_IP_Address.md)|Easy|Python3|[]|
|1295|[Find_Numbers_with_Even_Number_of_Digits](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Find_Numbers_with_Even_Number_of_Digits.md)|Easy|Python3|[Array]|
|1299|[Replace_Elements_with_Greatest_Element_on_Right_Side](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Replace_Elements_with_Greatest_Element_on_Right_Side.md)|Easy|Python3|[Array]|
|1344|[Angle_Between_Hands_of_a_Clock](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Angle_Between_Hands_of_a_Clock.md)|Medium|Python3|[Math]
|1346|[Check_If_N_and_Its_Double_Exist](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Check_If_N_and_Its_Double_Exist.md)|Easy|Python3|[Array]|