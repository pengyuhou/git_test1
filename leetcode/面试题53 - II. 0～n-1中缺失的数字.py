class Solution:
    def missingNumber(self, nums):
        l=len(nums)
        n=range(l+1)
        a={}
        for i in n:
            a[i] = 0
        for j in nums:
            a[j] += 1
        return [k for k,v in a.items() if v==0][0]
    
if __name__ == "__main__":
    n=[0,1,2,3,4,5,6,7,9]
    print(Solution().missingNumber(n))


