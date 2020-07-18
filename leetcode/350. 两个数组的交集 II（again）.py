class Solution(object):
    def intersect(self, nums1, nums2):
        ret = []
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                ret.append(i)
        return ret


if __name__ == "__main__":
    print(Solution().intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
