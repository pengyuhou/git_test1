class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        queue = [[0, 0]]
        ret = [[matrix[0][0]]]
        m, n = len(matrix), len(matrix[0])
        mark = [[False for _ in range(n)]for _ in range(m)]
        while queue:
            l = len(queue)
            tmp = []
            for _ in range(l):
                x, y = queue.pop(0)
                for dx, dy in [(0, 1), (1, 0)]:
                    xi = x + dx
                    yi = y + dy
                    if 0 <= xi < m and 0 <= yi < n and not mark[xi][yi]:
                            mark[xi][yi] = True
                            queue.append([xi,yi])
                            tmp.append(matrix[xi][yi])
            ret.append(tmp)
        for i in range(len(ret)):
            if not i%2:
                ret[i].reverse()
        res = []
        for i in ret:
            res += i

        return res


print(Solution().findDiagonalOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))