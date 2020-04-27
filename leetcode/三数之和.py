a = [-1, 0, 1, 2, -1, -4]

class Solution(object):

    def threeSum(self, nums):
        a_total = []
        for i in range(len(nums)-2):
            for j in (i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    a=[]
                    if nums[i] + nums[j]+nums[k]==0:
                        a.append(nums[i])
                        a.append(nums[j])
                        a.append(nums[k])
                        a_total.append(a)
        return a_total




s=Solution()
print(s.threeSum(a))




