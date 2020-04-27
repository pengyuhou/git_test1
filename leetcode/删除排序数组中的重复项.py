nums = [1,1,2]





class Solution(object):
    def removeDuplicates(self, nums):
        x = list(set(nums))

        x.sort()
        for i in range(len(x)):
            nums[i] = x[i]
        return len(x)


s=Solution()
print(s.removeDuplicates(nums))




