class Solution:
    def findMagicIndex(self, nums):
        for i in range(len(nums)):
            if i == nums[i]:
                return i
        return -1


if __name__ == "__main__":
    nums = [1, 1, 1]
    print(Solution().findMagicIndex(nums))


