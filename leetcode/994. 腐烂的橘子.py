class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        bad=[]
        good=[]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    good.append([i,j])
                if grid[i][j]==2:
                    bad.append([i,j])
        count = 0
        while good:
            ret = []
            for x,y in bad:
                for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                    xi = x+dx
                    yi = y+dy
                    if m > xi > -1 and n > yi > -1:
                        if [xi,yi] in good:
                            good.remove([xi,yi])
                            ret.append([xi,yi])
            if ret:
                bad += ret
                count += 1
            else:
                return -1
        return count



if __name__ == "__main__":
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    grid = [[0,2]]

    print(Solution().orangesRotting(grid))

