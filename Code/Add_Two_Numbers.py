# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # Create a new ListNode as head of returned linked list
        head = ListNode(0)

        n1, n2, carry, curr = 0, 0, 0, head
        
        while l1 or l2 or carry:
            
            # Check whether the current node is None, if true, assign it to the variable, otherwise the variable value is 0
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            
            # The divmod() method takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.
            carry, out = divmod(n1 + n2 + carry, 10)
            curr.next = ListNode(out)
            curr = curr.next
            # Or can just use // and %
            # curr.next = ListNode((n1 + n2 + carry)%10)
            # curr = curr.next
            # carry = (n1 + n2 + carry) // 10
            
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        
        return head.next