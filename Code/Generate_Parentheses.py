class Solution:
    def generateParenthesis(self, n: int, flag = 0) -> List[str]:
        if n > 0 and flag >= 0:
            return ['(' + p for p in self.generateParenthesis(n - 1, flag + 1)] + [')' + p for p in self.generateParenthesis(n, flag - 1)]
        return [')' * flag] * (not n)