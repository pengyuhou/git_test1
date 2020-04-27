class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        cp = triangle.copy()
        for i in range(len(cp)):
            for j in range(len(cp[i])):
                if i == 0:
                    continue
                if j == 0:
                    cp[i][j] += cp[i - 1][j]
                    continue
                if j == len(cp[i]) - 1:
                    cp[i][j] += cp[i - 1][j - 1]
                    continue
                cp[i][j] += min(cp[i - 1][j], cp[i - 1][j - 1])
        return min(cp[-1])



if __name__ == "__main__":
    nums = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(Solution().minimumTotal(nums))
