class Solution(object):
    def generateMatrix(self, n):
        ans=[]
        for i in range(n):
            ret=[]
            for j in range(n):
                ret.append(None)
            ans.append(ret)
        x = 0
        y = 0
        dx = 0
        dy = 1
        for i in range(1,n**2+1):
            ans[x][y]=i
            if 0<=x+dx<n and 0<=y+dy<n:
                if ans[x+dx][y+dy]!=None:
                    dx,dy = dy,-dx
                x += dx
                y += dy
            else:
                dx, dy = dy, -dx
                x += dx
                y += dy
        return ans


if __name__ == "__main__":
    print(Solution().generateMatrix(4))