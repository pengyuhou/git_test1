class Solution:
    def sumNums(self, n: int) -> int:
        if n == 1:
            return 1
        return self.sumNums(n - 1) + n


print(Solution().sumNums(9))
