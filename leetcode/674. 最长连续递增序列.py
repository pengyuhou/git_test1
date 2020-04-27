class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = len(nums)
        index = 0
        ret = 0
        while index < l - 1:
            res = 0
            while nums[index] < nums[index + 1]:
                res += 1
                index += 1
                if index >= l-1:
                    if res > ret:
                        ret = res
                    return ret+1
            index += 1
            if res > ret:
                ret = res
        return ret+1


if __name__ == "__main__":
    nums = []
    print(Solution().findLengthOfLCIS(nums))











