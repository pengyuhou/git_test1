class Solution(object):
    def respace(self, dictionary, sentence):
        l = len(sentence)
        dp = [0 for _ in range(l + 1)]
        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + 1
            for j in range(i - 1, -1, -1):
                if sentence[j:i] in dictionary:
                    dp[i] = min(dp[i], dp[j])
        return dp[-1]


if __name__ == '__main__':
    print(Solution().respace(dictionary=["looked", "just", "like", "her", "brother"]
                             , sentence="jesslookedjustliketimherbrother"))
