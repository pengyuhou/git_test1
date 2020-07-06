# class Solution(object):
#     def isMatch(self, s, p):
#         dp = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
#         dp[0][0] = True
#
#         for i in range(1, len(dp)):
#             if p[i - 1] == '*':
#                 dp[i][0] = dp[i - 1][0]
#
#         for i in range(1, len(dp)):
#             for j in range(1, len(dp[0])):
#                 if s[j - 1] == p[i - 1] and dp[i - 1][j - 1]:
#                     dp[i][j] = True
#                 if p[i - 1] == '?' and dp[i - 1][j - 1]:
#                     dp[i][j] = True
#                 if p[i - 1] == '*' and (dp[i - 1][j] or dp[i][j - 1]):
#                     dp[i][j] = True
#         return dp[-1][-1]


class Solution(object):
    def isMatch(self, s, p):
        import functools
        @functools.lru_cache(None)
        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            if i < len(s) and s[i] == p[j] and dfs(i + 1, j + 1):
                return True
            if i < len(s) and p[j] == '?' and dfs(i + 1, j + 1):
                return True
            if p[j] == '*':
                if i < len(s) and (dfs(i + 1, j + 1) or dfs(i + 1, j)):
                    return True
                if dfs(i, j + 1):
                    return True
            return False
        return dfs(0, 0)


print(Solution().isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab",
"***bba**a*bbba**aab**b"))
