class Solution(object):
    def maxArea(self, height):
        nums = height
        l = len(nums)
        index1 = 0
        index2 = l - 1
        max_V = 0
        while index2 > index1:

            max_V = max(max_V,min(nums[index1], nums[index2]) * (index2 - index1))
            if nums[index1]<nums[index2]:
                index1 += 1
            else:
                index2 -= 1
        return max_V

if __name__ == "__main__":
    nums = [1,2,4,3]
    print(Solution().maxArea(nums))
















