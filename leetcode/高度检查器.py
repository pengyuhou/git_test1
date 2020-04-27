class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        h = []
        for i in heights:
            h.append(i)
        index = 0
        heights.sort()
        for i, j in zip(heights, h):
            if i != j:
                index += 1
        return index




if __name__ == '__main__':
    heights = [1, 1, 4, 2, 1, 3]
    s=Solution()
    print(s.heightChecker(heights))








