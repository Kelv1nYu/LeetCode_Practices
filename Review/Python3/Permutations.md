**46. [Permutations.py](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Permutations.py)**      Level: Medium

中文：

* 使用 Backtracking(回溯) / DFS 算法递归寻找可能的排列方式，并存储到 result 中；
* 也可使用迭代算法循环找到可能的排列方式，并存储到 result 中:
    * 例如，如果输入`[1, 2, 3]`则首先将`1`添加到 List 中;
    * 然后，可以在前面或后面添加`2`。因此，我们必须复制答案列表（只是`[1]`），在`[1]`的位置`0`添加`2`，然后再次复制原始的`[1]`，然后添加`2`在位置`1`。现在我们得到的答案是`[[2, 1]，[1, 2]]`；
    * 然后我们必须添加`3`。首先复制`[2, 1]`和`[1, 2]`，在位置`0`添加`3`；然后复制`[2,1]`和`[1,2]`，并将`3`添加到位置`1`，然后对位置`3`执行相同的操作。

English:

* Use Backtracking / DFS algorithm to recursively find possible arrangements and store them in result;
* Iterative algorithm can also be used to find possible arrangements and store them in result:
    * For example, if the input is `[1, 2, 3]`, first add `1` to the List;
    * Then, you can add `2` before or after. Therefore, we have to copy the answer list (just `[1]`), add `2` at the position of index `0`, then copy the original `[1]` again, and then add `2` at the index `1`. Now the answer we get is `[[2, 1], [1, 2]]`;
    * Then we must add `3`. First copy `[2, 1]` and `[1, 2]`, add `3` at index `0`; then copy `[2,1]` and `[1,2]`, and add `3 ` to index `1`, then do the same for index `2`.