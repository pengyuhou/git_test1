class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        l = len(nums)
        thres = l // 3
        index = 0
        ret = []
        while index < l:
            count = 1
            while index + 1 < l and nums[index] == nums[index + 1]:
                count += 1
                index += 1
            if count > thres:

                ret.append(nums[index])

            index += 1
        return ret


if __name__ == "__main__":
    print(Solution().majorityElement([1,1,1,3,3,2,2,2]))
    
