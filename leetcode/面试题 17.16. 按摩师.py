class Solution(object):
    def massage(self, nums):
        l = len(nums)
        if l==0:
            return 0
        if l==1:
            return nums[0]
        if l==2:
            return max(nums)
        if l>=3:
            ret=[nums[0],max(nums[:2])]
            index = 2
            while index<l:
                ret.append(max(ret[index-1],ret[index-2]+nums[index]))
                index += 1
            return ret[-1]

if __name__ == "__main__":
    nums =[]
    print(Solution().massage(nums))









