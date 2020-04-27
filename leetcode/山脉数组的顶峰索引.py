class Solution(object):
    def peakIndexInMountainArray(self, A):
        nums=A
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i

if __name__ == "__main__":
    nums = [0,2,1,0]
    print(Solution().peakIndexInMountainArray(nums))










