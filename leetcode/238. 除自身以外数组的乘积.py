class Solution(object):
    def productExceptSelf(self, nums):
        if nums==[0]:
            return [1]
        if nums.count(0)>1:
            return [0]*len(nums)
        if nums.count(0)==1:
            count = 1
            for num in nums:
                count *= num
            for i in range(len(nums)):
                if not nums[i]:
                    nums[i]=count
                else:
                    nums[i] = 0
            return nums
        count = 1
        for num in nums:
            count *= num
        return [ count//i for i in nums]



if __name__ == "__main__":

    print(Solution().productExceptSelf([0,0]))







