class Solution:
    def hasAlternatingBits(self, n: int):
        res = list(bin(n)[2:])
        for i in range(1, len(res)):
            if res[i] == res[i - 1]:
                return False
        return True


print(Solution().hasAlternatingBits(10))
