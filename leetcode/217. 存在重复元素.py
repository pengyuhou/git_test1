class Solution:
    def containsDuplicate(self, nums):
        if len(nums)-len(set(nums)):
            return True
        else:
            return False



if __name__ == "__main__":
    nums =  [1,1,1,3,3,4,3,2,4,2]
    print(Solution().containsDuplicate(nums))


