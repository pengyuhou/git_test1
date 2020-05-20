# class Solution(object):
#     def kSmallestPairs(self, nums1, nums2, k):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         ret = []
#         for i in nums1:
#             for j in nums2:
#                 ret.append([i, j])
#         res = sorted(ret, key=lambda x: x[0] + x[1])
#         return res[:k]


class Solution:
    def fun(self, x):
        return x[0] + x[1]

    def kSmallestPairs(self, nums1, nums2, k):
        ret = []
        for i in nums1:
            for j in nums2:
                ret.append([i, j])

        def recur(p):
            if not p:
                return []
            l = len(p)
            if l == 1:
                return p
            mid = l // 2
            ret = []
            left = recur(p[:mid])
            right = recur(p[mid:])
            index1 = 0
            index2 = 0
            while index1 < len(left) and index2 < len(right):
                if self.fun(left[index1]) < self.fun(right[index2]):
                    ret.append(left[index1])
                    index1 += 1
                else:
                    ret.append(right[index2])
                    index2 += 1
            ret += left[index1:]
            ret += right[index2:]
            return ret
        return recur(ret)[:k]


if __name__ == "__main__":
    print(Solution().kSmallestPairs(nums1=[], nums2=[], k=2))
