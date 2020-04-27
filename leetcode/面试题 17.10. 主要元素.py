class Solution(object):
    def majorityElement(self, nums):
        a = list(set(nums))
        l = len(nums)
        for i in a:
            if nums.count(i) > l//2:
                return i
        return -1



if __name__ == "__main__":
    nums = [1,2,5,9,5,9,5,5,5]
    print(Solution().majorityElement(nums))


