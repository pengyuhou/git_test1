class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        dp = [[None for _ in range(l + 1)] for _ in range(l + 1)]
        lx = len(dp)
        for i in range(1, lx):
            for j in range(1, lx):
                if i == j:
                    dp[i][j] = True
        for i in range(1, lx):
            for j in range(1, i + 1):
                if i - j == 1:
                    if s[i - 1] == s[j - 1]:
                        dp[j][i] = True
                    continue
                if i != j:
                    if s[i - 1] == s[j - 1] and dp[j + 1][i - 1]:
                        dp[j][i] = True
                    else:
                        dp[j][i] = False
        return sum([i.count(1) for i in dp])


print(Solution().countSubstrings('ttyyuuiiooppllkkjjhhmfafda'))
