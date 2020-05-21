class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ''
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(dp)):
            for j in range(i + 1):
                if i == j:
                    dp[j][i] = True
                    if len(s[j:i + 1]) > len(ret):
                        ret = s[j:i + 1]
                    continue
                if i - j == 1 and s[i] == s[j]:
                    dp[j][i] = True
                    if len(s[j:i + 1]) > len(ret):
                        ret = s[j:i + 1]
                    continue
                if s[i] == s[j] and dp[j + 1][i - 1]:
                    dp[j][i] = True
                    if len(s[j:i + 1]) > len(ret):
                        ret = s[j:i + 1]
        return ret


if __name__ == "__main__":
    print(Solution().longestPalindrome("asdasdqdqdas"))
