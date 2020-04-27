class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
        return len(nums)


if __name__ == "__main__":
    nums = [2,0,1,4]
    print(Solution().missingNumber(nums))








