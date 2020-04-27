class Solution:
    def findLHS(self, nums):
        a={}
        for num in nums:
            if num not in a.keys():
                a[num]=1
            else:
                a[num] += 1
        ret = 0
        for i in a.keys():
            if i+1 in a.keys():
                if a[i]+a[i+1]>ret:
                    ret=a[i]+a[i+1]
        return ret

if __name__ == "__main__":
    nums = [1,3,2,2,5,2,3,7]
    print(Solution().findLHS(nums))




