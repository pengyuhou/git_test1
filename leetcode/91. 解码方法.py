# class Solution:
#     def numDecodings(self, s: str) -> int:
#         if not s:
#             return 0
#         ret = []
#         def dfs(index, res):
#             if index >= len(s):
#                 if res.copy() not in ret:
#                     ret.append(res.copy())
#                 return
#             for i in [1, 2]:
#                 if 1 <= int(s[index:index + i]) <= 26 and not s[index:index + i].startswith('0'):
#                     res.append(int(s[index:index + i]))
#                     dfs(index + i, res)
#                     res.pop()
#         dfs(0, [])
#         return len(ret)

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        if not s:
            return 0

        dp[1] = 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp[i + 1] = dp[i - 1]
                else:
                    return 0
                continue
            if s[i - 1] == '1':
                dp[i + 1] = dp[i] + dp[i - 1]
                continue
            if s[i - 1] == '2' and '1' <= s[i - 1] <= '6':
                dp[i + 1] = dp[i] + dp[i - 1]
                continue
            dp[i+1] = dp[i]
        return dp[-1]


if __name__ == "__main__":
    print(Solution().numDecodings(
        "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"))
