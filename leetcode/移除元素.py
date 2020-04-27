nums=[3,2,2,3]
val=3


class Solution(object):
    def removeElement(self, nums, val):
        a=[]
        for i in nums:
            if i!=val:
                a.append(i)
        for i in range(len(a)):
            nums[i] = a[i]
        return len(a)


s=Solution()
print(s.removeElement(nums, val))
