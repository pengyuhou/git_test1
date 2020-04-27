class Solution(object):
    def lengthOfLIS(self, nums):

        if nums==[]:
            return 0
        l = len(nums)
        dp=[1]*l

        for i in range(l-1):
            for j in range(i+1,l):
                if nums[i]<nums[j]:
                    dp[j]=max(dp[i]+1,dp[j])

        return max(dp)




if __name__ == "__main__":
    nums =  [2,5,3,7,101]
    nums = [1,3,1]
    # nums= [1,2,4,1]
    # nums = [10,9,2,5,3,7,101,18]
    nums = [2,2]
    # nums = [1,3,6,7,9,4,10,5,6]
    # nums=[0]
    nums = [10,22,9,33,21,50,41,60,80]
    print(Solution().lengthOfLIS(nums))

