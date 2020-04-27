class Solution(object):
    def findShortestSubArray(self, nums):
        if nums==[]:
            return 0
        l = len(nums)
        nums_cp=nums.copy()
        nums_cp.reverse()
        a={}
        for i in nums:
            if i not in a.keys():
                a[i] = 1
            else:
                a[i] += 1
        res=max(a.values())
        ret = []
        for i in a.keys():
            if a[i] == res:
                index1 = nums.index(i)
                index2 = l - nums_cp.index(i)
                ret.append(index2-index1)
        return min(ret)

if __name__ == "__main__":
    nums =  [1,2,2,3,2,4,2]
    # nums = [1,1,1,2,1]
    nums = [1,2,2,3,1]

    print(Solution().findShortestSubArray(nums = nums))
