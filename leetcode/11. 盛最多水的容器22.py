class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        index1 = 0
        index2 = len(height) - 1
        max_water = -float('inf')
        while index1 < index2:
            max_water = max(min(height[index1], height[index2]) * (index2 - index1), max_water)
            if nums[index1] < nums[index2]:
                index1 += 1
            else:
                index2 -= 1
        return max_water


if __name__ == "__main__":
    nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(nums))
