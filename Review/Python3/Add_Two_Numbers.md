**2. [Add_Two_Numbers.py](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Add_Two_Numbers.py)**      Level: Medium

中文：
* 创建一个新的节点作为返回链表的头；
* 当 l1 存在或 l2 存在或carry存在时继续循环进行加和过程；
* 使用divmod方法得到当前 l1 节点值，l2 节点值 和 carry的和，并将其除以10，将商和余数分别赋值给carry和out；
* 将当前节点的next指向值为out的新节点；
* 若循环尚未结束则对剩余节点做相同处理，若结束则返回头结点的next。

English:

* Create a new node as the head of the returned list;
* When l1 exists, l2 exists, or carry exists, continue the loop of addition process;
* Use the divmod method to get the sum of values of current l1, l2 node and carry, divide it by 10, and assign the quotient and remainder to carry and out respectively;
* Point the next node of the current node to the new node whose value is out;
* If the loop has not ended, do the same processing to the remaining nodes, if it ends, return to the next of the head node.