class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1 = set(nums1)
        s2 = set(nums2)
        x = s1 & s2
        x = list(x)

        for i in range(len(x)):
            num = min(nums1.count(x[i]), nums2.count(x[i]))
            x += [x[i]] * (num - 1)
        return x

if __name__ == "__main__":
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(Solution().intersect(nums1,nums2))


    # print(x)
    # x=[12,3]
    # x+=[2]*4
    # print(x)







