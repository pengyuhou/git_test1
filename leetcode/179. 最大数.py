class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if int(str(nums[i])+str(nums[j])) <int(str(nums[j])+str(nums[i])):
                    nums[i],nums[j]=nums[j],nums[i]
        return ''.join([str(i) for i in nums])


if __name__ == "__main__":
    nums = [3,30,34,5,9]
    # nums = [10,2]
    print(Solution().largestNumber(nums))

