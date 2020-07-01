class Solution:
    def firstMissingPositive(self, nums):
        nums = list(set(nums))
        nums = [i for i in nums if i > 0]
        nums.sort()
        cur = 1
        for i in nums:
            if i != cur:
                return cur
            cur += 1
        return nums[-1] + 1 if nums else 1


print(Solution().firstMissingPositive([7, 8, 9, 11, 12]))

a = [[1, 2, 3], [1, 3], [2, 3], [1, 2, 3]]

print([list(i) for i in set([tuple(i) for i in a])])

