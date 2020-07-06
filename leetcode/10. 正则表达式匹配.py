class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
        dp[0][0] = True
        stack = []
        for i in range(1, len(dp)):
            stack.append(p[i - 1])
            if p[i - 1] == '*':
                stack.pop()
                stack.pop()
                if not stack:
                    dp[i][0] = True
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if p[i - 1] == s[j - 1] and dp[i - 1][j - 1]:
                    dp[i][j] = True
                if p[i - 1] == '.' and dp[i - 1][j - 1]:
                    dp[i][j] = True
                if p[i - 1] == '*' and (
                        ((p[i - 2] == s[j - 1] or p[i - 2] == '.') and dp[i][j - 1]) or dp[i - 1][j] or dp[i - 2][j]):
                    dp[i][j] = True
        return dp[-1][-1]


print(Solution().isMatch("ab",
                         ".*.."))
