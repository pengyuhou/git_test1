class Solution:
    def wordBreak(self, s: str, wordDict):
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(dp)):
            for word in wordDict:
                if s[i - len(word):i] == word and not dp[i]:
                    dp[i] = dp[i - len(word)]
        return dp[-1]


print(Solution().wordBreak(s="leetcod", wordDict=["leet", "code"]))
