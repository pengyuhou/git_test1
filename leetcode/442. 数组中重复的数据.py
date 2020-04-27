class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        ret = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                ret.append(nums[i])
        return ret





if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    print(Solution().findDuplicates(nums))