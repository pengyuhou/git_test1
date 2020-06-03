# class Solution:
#     ret = 0
#     def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
#         def dfs(x, y, cnt):
#             if cnt >= 0 and (x < 0 or x >= m or y < 0 or y >= n):
#                 self.ret += 1
#                 return
#             if cnt < 0:
#                 return
#             for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                 xi = x + dx
#                 yi = y + dy
#                 dfs(xi, yi, cnt - 1)
#         dfs(i, j, N)
#         return self.ret % (10 ** 9 + 7)
#
#
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp = [{} for _ in range(N + 1)]
        dp[0][(i, j)] = 1
        ret = 0
        for i in range(1, N + 1):
            for x, y in dp[i - 1]:
                count = dp[i - 1][(x, y)]
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    xi = x + dx
                    yi = y + dy
                    if xi < 0 or xi >= m or yi < 0 or yi >= n:
                        ret += count
                    elif (xi, yi) in dp[i]:
                        dp[i][(xi, yi)] += count
                    else:
                        dp[i][(xi, yi)] = count
        return ret

class Solution:
    d = {}
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        def dfs(x, y, cnt):
            if cnt > N:
                return 0
            if x < 0 or x >= m or y < 0 or y >= n:
                return 1
            ret = []
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                xi = x + dx
                yi = y + dy
                if (xi, yi, cnt + 1) not in self.d:
                    self.d[(xi, yi, cnt + 1)] = dfs(xi, yi, cnt + 1)
                else:
                    ret.append(self.d[xi, yi, cnt + 1])
            ret = 0
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                xi = x + dx
                yi = y + dy
                ret += self.d[xi, yi, cnt + 1]
            return ret
        return dfs(i, j, 0) % (10 ** 9 + 7)

print(Solution().findPaths(m=1, n=2, N=50, i=0, j=0))
