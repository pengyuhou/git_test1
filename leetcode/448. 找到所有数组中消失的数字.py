class Solution:
    def findDisappearedNumbers(self, nums):
        l = len(nums)
        n = set(nums)
        ret = []
        for i in range(1,l+1):
            if i not in n:
                ret.append(i)
        return ret

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    print(Solution().findDisappearedNumbers(nums))
