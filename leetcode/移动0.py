class Solution:
    def moveZeroes(self, nums):
        # for i in range(len(nums) - 1):
        #     for j in range(len(nums) - 1 - i):
        #         if nums[j] == 0 and nums[j + 1] != 0:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)



if __name__ == "__main__":
    nums=[]
    Solution().moveZeroes(nums)
    print(nums)







