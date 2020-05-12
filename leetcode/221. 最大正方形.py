class Solution(object):
    def maximalSquare(self, matrix):
        if matrix == [] or matrix == [[]]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    if matrix[i][j] == '1':
                        dp[i][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1' and matrix[i][j - 1] == '1' and matrix[i - 1][j] == '1' and matrix[i - 1][
                    j - 1] == '1':
                    if dp[i - 1][j - 1] == dp[i - 1][j] == dp[i][j - 1]:
                        dp[i][j] = int(dp[i - 1][j - 1] ** 0.5 + 1) ** 2
                        continue
                    else:
                        res = min([dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]])

                        dp[i][j] = (int(res ** 0.5) + 1) ** 2
                        continue
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                    continue
                dp[i][j] = 1
        ret = []
        for i in dp:
            ret.append(max(i))
        return max(ret)


if __name__ == "__main__":
    nums = [["1", "1", "1", "0", "0"], ["1", "1", "1", "0", "0"], ["1", "1", "1", "1", "1"], ["0", "1", "1", "1", "1"],
            ["0", "1", "1", "1", "1"], ["0", "1", "1", "1", "1"]]

    print(Solution().maximalSquare(nums))
