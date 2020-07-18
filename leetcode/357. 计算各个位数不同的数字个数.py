class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        from functools import lru_cache
        @lru_cache(None)
        def dfs(num):
            if num == 0:
                return 1
            ret = 9
            for i in range(num - 1):
                ret *= 9 - i
            return ret + dfs(num - 1)
        return dfs(n)


if __name__ == '__main__':
    print(Solution().countNumbersWithUniqueDigits(2))
