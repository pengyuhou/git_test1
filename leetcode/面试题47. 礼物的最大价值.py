class Solution:
    def maxValue(self, grid):
        m = len(grid)
        n = len(grid[0])
        ret = []
        for i in range(m):
            a = []
            for j in range(n):
                a.append(None)
            ret.append(a)
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    ret[i][j] = grid[i][j]
                else:
                    if i == 0:
                        ret[i][j] = grid[i][j] + ret[i][j - 1]
                    elif j == 0:
                        ret[i][j] = grid[i][j] + ret[i - 1][j]
                    else:
                        ret[i][j] = max(ret[i][j - 1], ret[i - 1][j]) + grid[i][j]
        return ret[-1][-1]

"""
输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物

"""

if __name__ == "__main__":
    grid = [ [1,3,1],
             [1,5,1],
             [4,2,1] ]
    print(Solution().maxValue(grid))



















