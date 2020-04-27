class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = {}
        for j in set(nums):
            a[j] = 0

        for i in nums:
            a[i] = a[i] + 1
        l = len(nums)
        max_num = max(a.values())
        return list(a.keys())[list(a.values()).index(max_num)]


if __name__ == '__main__':
    nums=[2,2,1,1,1,2,2]
    a={}
    for j in set(nums):
        a[j]=0


    for i in nums:
        a[i]=a[i]+1
    print(a)
    l=len(nums)
    max_num=max(a.values())
    print(list(a.values()))
    print(list(a.values()).index(3))


    # print(list(a.keys())[list(a.values()).index(max_num)])


    # print(list(a.keys())[list(a.values()).index(10)])
    # s=Solution()
    # print(s.majorityElement(nums))




