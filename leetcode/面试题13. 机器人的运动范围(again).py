class Solution:
    def fun(self, x, y):
        return sum([int(i) for i in list(str(x))]) + sum([int(i) for i in list(str(y))])

    def movingCount(self, m: int, n: int, k: int) -> int:

        queue = [[0, 0]]
        mark = [[False for _ in range(n)] for _ in range(m)]
        mark[0][0] = True
        count =1
        while queue:
            l = len(queue)
            for _ in range(l):
                a = queue.pop(0)
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    xi = a[0] + dx
                    yi = a[1] + dy
                    if 0 <= xi < m and 0 <= yi < n and self.fun(xi, yi) <= k and not mark[xi][yi]:
                        mark[xi][yi] = True
                        queue.append([xi, yi])
                        count += 1
        return count


if __name__ == "__main__":
    print(Solution().movingCount(1, 2, 1))
