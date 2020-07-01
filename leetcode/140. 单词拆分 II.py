class Solution(object):
    def wordBreak(self, s, wordDict):
        ret = []
        def dfs(p, index, res):
            if index >= len(s):
                ret.append(' '.join(res.copy()))
            for j in range(len(p)):
                if s[index:index + len(p[j])] == p[j]:
                    res.append(p[j])
                    dfs(p, index + len(p[j]), res)
                    res.pop()
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(dp)):
            for word in wordDict:
                if not dp[i] and s[i - len(word):i] == word:
                    dp[i] = dp[i - len(word)]
        if dp[-1]:
            dfs(wordDict, 0, [])
            return ret
        else:
            return []


if __name__ == "__main__":
    print(Solution().wordBreak("pineapplepenapple",
                               ["apple", "pen", "applepen", "pine", "pineapple"]))
