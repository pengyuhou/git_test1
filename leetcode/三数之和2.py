a = [-1, 0, 1, 2, -1, -4]

class Solution(object):

    def threeSum(self, nums):
        a_total = []
        for i in range(len(nums)-1):
            for j in range(len(nums)-1):
                for k in range(len(nums)-1):
                    if i!=j and i!=k and j!=k:
                        if nums[i]+nums[j]+nums[k]==0:
                            a = []
                            a.append(nums[i])
                            a.append(nums[j])
                            a.append(nums[k])
                            a_total.append(a)


        return a_total


S=Solution()
print(S.threeSum(a))