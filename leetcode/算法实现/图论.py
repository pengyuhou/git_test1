import numpy as np


class Solution:
    def fun(self):

        mat = [[float('inf') for _ in range(11)] for _ in range(11)]
        for i in range(11):
            for j in range(11):
                if i == j:
                    mat[i][j] = 0
        res = [[(1, 2), (2, 8), (3, 1)],
               [(0, 2), (2, 6), (4, 1)],
               [(0, 8), (1, 6), (3, 7), (4, 5), (5, 1), (6, 2)],
               [(0, 1), (2, 7), (3, 0), (6, 9)],
               [(1, 1), (2, 5), (5, 3), (7, 2), (8, 9)],
               [(2, 1), (4, 3), (6, 4), (8, 6)],
               [(2, 2), (3, 9), (5, 4), (8, 3), (9, 1)],
               [(4, 2), (8, 7), (10, 9)],
               [(4, 9), (5, 6), (6, 3), (7, 7), (9, 1), (10, 2)],
               [(6, 1), (8, 1), (10, 4)],
               [(7, 9), (8, 2), (9, 4)],
               ]
        res = enumerate(res)
        for i, j in res:
            for x1, x2 in j:
                mat[i][x1] = x2

        dp = [float('inf') for _ in range(11)]
        # print(dp)
        dp[0] = 0
        print(np.array(mat))
        print('----')
        for i in range(11):
            for j in range(11):
                if mat[i][j] != float('inf') and i != j:
                    dp[i] = min(dp[i], dp[j] + mat[i][j])

                    # print(dp)
        return dp


class Solution1:
    print('---')

    def fun(self):
        res = [[(1, 2), (2, 8), (3, 1)],
               [(0, 2), (2, 6), (4, 1)],
               [(0, 8), (1, 6), (3, 7), (4, 5), (5, 1), (6, 2)],
               [(0, 1), (2, 7) , (6, 9)],
               [(1, 1), (2, 5), (5, 3), (7, 2), (8, 9)],
               [(2, 1), (4, 3), (6, 4), (8, 6)],
               [(2, 2), (3, 9), (5, 4), (8, 3), (9, 1)],
               [(4, 2), (8, 7), (10, 9)],
               [(4, 9), (5, 6), (6, 3), (7, 7), (9, 1), (10, 2)],
               [(6, 1), (8, 1), (10, 4)],
               [(7, 9), (8, 2), (9, 4)]]
        # res = [
        #     [(1, 1), (2, 2), (3, 3)],
        #     [(0, 1), (2, 1), (4, 3)],
        #     [(0, 2), (1, 1), (3, 0), (4, 2)],
        #     [(0, 3), (2, 0), (4, 1)],
        #     [(1, 3), (2, 2), (3, 1)]
        # ]
        dp = [float('inf') for _ in range(len(res))]

        dp[0] = 0
        for i in range(len(res)):
            for j, k in res[i]:
                dp[j] = dp[j] if  dp[j] < dp[i] + k else dp[i] + k
        return dp


if __name__ == "__main__":
    print(Solution1().fun())
