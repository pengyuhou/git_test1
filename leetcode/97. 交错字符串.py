class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def dfs(cur1, cur2, res):
            if len(res) == len(s3) and cur1 == len(s1) + 1 and cur2 == len(s2) + 1:
                if ''.join(res.copy()) == s3:
                    return True
                return False
            for i in range(cur1, len(s1) + 2):
                for j in range(cur2 + 1, len(s2) + 2):
                    tmp = res[:]
                    res += list(s1[cur1:i])
                    res += list(s2[cur2:j])
                    if dfs(i, j, res):
                        return True
                    res[:] = tmp
            return False
        return dfs(0, 0, [])


class Solution:
    def isInterleave(self, s1, s2, s3):
        if s1 == s2 == s3 == '':
            return True
        if len(s1) + len(s2) < len(s3) or len(s1) + len(s2) > len(s3):
            return False
        dp = [[False for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0 and j != 0:
                    if s1[:j] == s3[:j]:
                        dp[i][j] = True
                if j == 0 and i != 0:
                    if s2[:i] == s3[:i]:
                        dp[i][j] = True
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if dp[i - 1][j]:
                    if s2[i - 1] == s3[i + j - 1]:
                        dp[i][j] = True
                        continue
                if dp[i][j - 1]:
                    if s1[j - 1] == s3[i + j - 1]:
                        dp[i][j] = True
                        continue
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().isInterleave("",
                                  "",
                                  ""))
