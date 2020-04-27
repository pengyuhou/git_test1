class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = min(nums)
        count = 0
        for i in nums:
            count += i - min_val
        return count


if __name__ == "__main__":
    print(Solution().minMoves([1, 2, 3]))
