class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        ret = []
        for i in range(m):
            for j in range(n):
                ret.append(matrix[i][j])
        return sorted(ret)[k-1]



if __name__ == "__main__":
    print(Solution().kthSmallest(matrix=[
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ],
        k=8))
