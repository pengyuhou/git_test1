class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        if len(nums)==1:
            return nums[0]
        nums1 = nums[1:]
        nums2 = nums[:-1]
        dp1 = [0 for _ in range(len(nums1)+1)]
        dp2 = [0 for _ in range(len(nums2)+1)]
        dp1[1] = nums1[0]
        dp2[1] = nums2[0]
        for i in range(2,len(dp1)):
            dp1[i] = max(dp1[i-1],dp1[i-2]+nums1[i-1])
        for i in range(2,len(dp2)):
            dp2[i] = max(dp2[i-1],dp2[i-2]+nums2[i-1])

        return max(dp1[-1],dp2[-1])



if __name__ == "__main__":
    nums = [2]
    print(Solution().rob(nums))
















