class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        ret = []

        def dfs(num):
            if len(ret) == k:
                return ret[-1]
            if num > n:
                return
            ret.append(num)
            for i in range(10):
                q = dfs(num * 10 + i)
                if q:
                    return q

        for i in range(1, 10):
            res = dfs(i)
            if res:
                return res


print(Solution().findKthNumber(7747794, 5857460))
