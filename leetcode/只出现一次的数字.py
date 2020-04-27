class Solution(object):
    def singleNumber(self, nums):
        a={}
        for i in nums:
            if i not in a.keys():
                a[i] = 1
            else:
                a[i] += 1
        k=list(a.keys())
        v=list(a.values())
        return k[v.index(1)]

if __name__ == '__main__':

    nums=[4,1,2,1,2]
    print(Solution().singleNumber(nums))


