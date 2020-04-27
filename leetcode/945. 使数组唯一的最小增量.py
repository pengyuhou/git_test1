class Solution(object):
    def minIncrementForUnique(self, A):
        if A == []:
            return 0
        A.sort()
        a=A
        l = len(a)
        res = range(a[0],a[0]+l)
        count = 0
        res=list(res)
        for i in range(l):
            if res[i]<a[i]:
                res[i:] = range(a[i],a[i]+l-i)
        for i in range(l):
            if a[i]<res[i]:
                count += res[i]-a[i]
        return count



if __name__ == "__main__":
    nums = [3]
    nums = [1,2,2]



    print(Solution().minIncrementForUnique(nums))







