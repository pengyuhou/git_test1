class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[0] < 0 and nums[1] < 0:
            if nums[-1] * nums[-2] * nums[-3] >= nums[0] * nums[1] * nums[-1]:
                return  nums[-1] * nums[-2] * nums[-3]
            else:
                return nums[0] * nums[1] * nums[-1]
        else:
            return nums[-1] * nums[-2] * nums[-3]

if __name__ == '__main__':
    nums=[4,1,3,2,-9,-8]
    s=Solution()
    print(s.maximumProduct(nums))



    # if nums[-1]*nums[-2]*nums[-3]



