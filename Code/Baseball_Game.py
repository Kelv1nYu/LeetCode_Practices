class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """

        # use stack as a storage
        stack = []

        # get op in ops
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))
        
        return sum(stack)