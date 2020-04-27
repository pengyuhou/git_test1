class Solution:
    def searchMatrix(self, matrix, target):
        if matrix == [] or matrix==[[]]:
            return False
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][-1]:
                index1 = 0
                index2 = n - 1
                while index2 - index1 > 1 and matrix[i][index1] != target and matrix[i][index2] != target:
                    mid = (index1 + index2) // 2
                    if matrix[i][mid] < target:
                        index1 = mid
                    else:
                        index2 = mid
                if matrix[i][index1] == target or matrix[i][index2] == target:
                    return True
        return False


if __name__ == "__main__":
    mat = [[]]

    print(Solution().searchMatrix(mat,29))