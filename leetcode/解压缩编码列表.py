class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = len(nums) // 2
        ret = []
        for j in range(i):

            for k in range(nums[2 * j]):
                ret.append(nums[2 * j + 1])

        return ret



if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    # i = len(nums)//2
    # ret=[]
    # for j in range(i):
    #
    #     for k in range(nums[2*j]):
    #         ret.append(nums[2*j+1])
    #
    # print(ret)
    s=Solution()
    print(s.decompressRLElist(nums))




