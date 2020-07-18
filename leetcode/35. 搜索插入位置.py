class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import bisect
        return bisect.bisect_left(nums, target)


if __name__ == '__main__':
    # print(Solution().searchInsert([1, 3, 5, 6], 0))
    import bisect

    a = [1, 3, 5, 6]
    print(bisect.bisect_left(a, 5))
    bisect.insort(a,5)
    print(a)
