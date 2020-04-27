class Solution(object):
    def sortColors(self, nums):
        a={0:0,1:0,2:0}
        for i in set(nums):
            a[i] += nums.count(i)
        nums[:] = [0]*a[0]+[1]*a[1]+[2]*a[2]

print(Solution().sortColors([0]))
