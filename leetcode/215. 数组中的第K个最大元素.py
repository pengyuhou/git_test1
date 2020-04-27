class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        a=sorted(nums)
        return a[-k]



if __name__ == "__main__":

    print(Solution().findKthLargest( [3,2,3,1,2,4,5,5,6],4))

















