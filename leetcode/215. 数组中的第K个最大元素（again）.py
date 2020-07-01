class Solution(object):
    def findKthLargest(self, nums, k):
        return sorted(nums)[::-1][k-1]


print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], k=2))
