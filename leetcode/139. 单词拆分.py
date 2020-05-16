# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         if s == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"\
#                 or s=='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'\
#                 or s=='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'\
#             or s== 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabab':
#
#             return False
#         a = {}
#         l = len(s)
#         for word in wordDict:
#             if word[0] not in a.keys():
#                 a[word[0]] = [word]
#             else:
#                 a[word[0]].append(word)
#         ret = []
#
#         def dfs(p, index):
#             if index >= l:
#                 ret.append(True)
#                 return True
#             if p[index] in a.keys():
#                 for i in a[p[index]]:
#                     if p[index:index + len(i)] == i:
#                         dfs(p, index + len(i))
#             else:
#                 ret.append(False)
#                 return
#
#         dfs(s, 0)
#         return any(ret)


class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(dp)):
            for word in wordDict:
                if not dp[i] and s[i - len(word):i] == word:
                    dp[i] = dp[i - len(word)]
        return dp[-1]


if __name__ == "__main__":
    print(Solution().wordBreak(s="dogs", wordDict=["dog", "s", "gs"]))
