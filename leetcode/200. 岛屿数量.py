class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        nums = grid
        m, n = len(grid), len(grid[0])
        mark = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        for x in range(m):
            for y in range(n):
                if not mark[x][y] and int(nums[x][y]):
                    count += 1
                    mark[x][y] = True
                    nums[x][y] = '0'
                    queue = [[x, y]]
                    while queue:
                        xa, ya = queue.pop(0)
                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            xi = xa + dx
                            yi = ya + dy
                            if 0 <= xi < m and 0 <= yi < n and  int(nums[xi][yi]) and not mark[xi][yi]:
                                queue.append([xi,yi])
                                mark[xi][yi] = True
                                nums[xi][yi] = '0'
        return count



if __name__ == "__main__":
    nums = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    print(Solution().numIslands(nums))
