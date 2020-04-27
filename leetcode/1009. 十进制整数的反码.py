class Solution:
    def bitwiseComplement(self, N: int) -> int:
        n=N
        n=bin(n)[2:]
        res = [int(i) for i in n]
        index = len(res)-1
        amount = 0
        cur = 0
        while index >= 0:
            if res[index]==0:
                amount += 2**cur
            cur += 1
            index -= 1
        return amount


print(Solution().bitwiseComplement(10**9))
