class Solution(object):
    def isStraight(self, nums):
        if nums == []:
            return False
        count = 0
        res = [i for i in nums if i!=0 ]
        count =0
        for i in nums:
            if i==0:
               count += 1
        res.sort()
        l = len(res)
        if l==0 or l==1:
            return  True
        index = 0
        amount = 0
        while index<l-1:
            if res[index]==res[index+1]:
                return False
            amount += res[index+1]-res[index]
            index += 1
        if amount <= l-1+count:
            return True
        else:
            return False


print(Solution().isStraight([0,0,2,2,5]))









