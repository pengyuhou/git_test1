class Solution(object):
    def islandPerimeter(self, grid):
        count = 0
        l = len(grid)
        if l==1:
            return grid[0].count(1)*2+2
        for i in range(l):
            if 1 in grid[i]:
                count += 2
            if i == 0:
                for j in range(len(grid[0])):
                    if grid[0][j]:
                        count += 1
                        if not grid[1][j]:
                            count += 1
                x = [str(i) for i in grid[0]]
                x = ''.join(x)
                c = x.split('0')
                num = 0
                for x in c:
                    if '1' in x:
                        num += 1
                if num>1:
                    count += (num - 1) * 2
            elif i == l - 1:
                for j in range(len(grid[l - 1])):
                    if grid[l - 1][j]:
                        count += 1
                        if not grid[l - 2][j]:
                            count += 1
                x = [str(i) for i in grid[l-1]]
                x = ''.join(x)
                c = x.split('0')
                num = 0
                for x in c:
                    if '1' in x:
                        num += 1
                if num > 1:
                    count += (num - 1) * 2
            else:
                for j in range(len(grid[i])):
                    if grid[i][j]:
                        if not grid[i - 1][j]:
                            count += 1
                        if not grid[i + 1][j]:
                            count += 1
                x = [str(i) for i in grid[i]]
                x = ''.join(x)
                c = x.split('0')
                num = 0
                for x in c:
                    if '1' in x:
                        num += 1
                if num > 1:
                    count += (num - 1) * 2
        return count

if __name__ == "__main__":


    # grid = [[0,1,0,0],
    #         [1,1,1,0],
    #         [0,1,0,0],
    #         [1,1,0,0]]
    # grid = [[1,0]]
    grid = [[1,1,1],[1,0,1]]

    print(Solution().islandPerimeter(grid))

    # a=[1,0,1,1,1,0,1]
    # x=[str(i) for i in a]
    # x=''.join(x)
    # print(x)
    # print(x)
    # c=x.split('0')
    # print(c)
    # num=0
    # for x in c:
    #     if '1' in x:
    #         num += 1
    # print((num-1)*2)














