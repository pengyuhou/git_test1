class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ret = [[0 for _ in range(m) ] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    ret[i][j] = 1
        for i in range(n):
            for j in range(m):
                if ret[i][j]==0:
                    ret[i][j] = ret[i][j-1]+ret[i-1][j]
        return ret[-1][-1]










if __name__ == "__main__":
    print(Solution().uniquePaths(3,2))






