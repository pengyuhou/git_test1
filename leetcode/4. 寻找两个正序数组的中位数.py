class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        res = sorted(nums1 + nums2)
        l = len(res)
        mid = l // 2
        if l % 2:
            return res[mid]
        else:
            return (res[mid] + res[mid - 1]) / 2


print(Solution().findMedianSortedArrays(
    [],
    [2, 3]))
