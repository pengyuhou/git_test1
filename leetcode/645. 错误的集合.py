class Solution(object):
    def findErrorNums(self, nums):
        res2 = None
        b={}
        for i in nums:
            if i not in b.keys():
                b[i]=1
            else:
                res2 = i
                break
        x=list(set(nums))
        x.sort()
        l = len(x)
        for i in range(1,len(nums)+1):
            if i-1<l:
                if i != x[i-1]:
                    return [res2,i]
            else:
                return [res2,l+1]

if __name__ == "__main__":
    nums = [1,1]
    print(Solution().findErrorNums(nums))

