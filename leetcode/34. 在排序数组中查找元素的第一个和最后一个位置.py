class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        ret = []
        for i in range(len(nums)):
            if nums[i] == target:
                ret.append(i)
                break
        if not ret:
            ret=[-1]
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == target:
                ret.append(i)
                break
        if ret==[-1]:
            ret += [-1]
        return ret
        """






if __name__ == "__main__":
    nums = [3,3,3]
    target = 3
    print(Solution().searchRange(nums, target))
