# class Solution(object):
#     def nextGreaterElement(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         ret = []
#         index = len(nums2) - 1
#         for i in nums1:
#             flag = i
#
#             for j in range(index, -1, -1):
#                 if nums2[j] > i:
#                     flag = nums2[j]
#                 if nums2[j] == i:
#                     break
#             if flag != i:
#                 ret.append(flag)
#             else:
#                 ret.append(-1)
#         return ret


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack, hashmap = list(), dict()
        for i in nums2:
            while len(stack) != 0 and stack[-1] < i:
                hashmap[stack.pop()] = i
            stack.append(i)
        return [hashmap.get(i,-1) for i in nums1]


if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    s=Solution()
    print(s.nextGreaterElement(nums1,nums2))
















