class Solution:
    def findRepeatNumber(self, nums):
        a = {}
        for num in nums:
            if num not in a.keys():
                a[num] = 1
            else:
                return num



if __name__ == "__main__":
    nums=[2, 3, 1, 0, 2, 5, 3]
    print(Solution().findRepeatNumber(nums))





