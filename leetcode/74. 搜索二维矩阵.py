class Solution(object):
    def searchMatrix(self, matrix, target):
        if matrix == [] or matrix == [[]]:
            return False
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][-1]:
                left = 0
                right = n - 1
                while right - left > 1 and matrix[i][left] != target and matrix[i][right] != target:
                    mid = (left + right) // 2
                    if matrix[i][mid] > target:
                        right = mid
                    else:
                        left = mid
                if matrix[i][left] == target or matrix[i][right] == target:
                    return True

                        # left = 0
                        # right = n - 1
                        # while right - left > 1 and matrix[i][left] != target and matrix[i][right] != target:
                        #     mid = (left + right) // 2
                        #     if matrix[i][mid]<target:
                        #         left = mid
                        #     else:
                        #         right =mid
                        # if matrix[i][left] ==target or matrix[i][right]==target:
                        #     return True
        return False


if __name__ == "__main__":
    mat = [[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 50]]
    print(Solution().searchMatrix(mat, 4))
