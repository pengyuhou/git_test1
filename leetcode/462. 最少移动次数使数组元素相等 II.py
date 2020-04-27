class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l = len(nums)
        mid = l//2
        count = 0
        for i in nums:
            count += abs(i-nums[mid])
        return count







if __name__ == "__main__":

    print(Solution().minMoves2([1,2,3]))











