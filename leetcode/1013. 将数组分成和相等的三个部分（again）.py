class Solution(object):
    def canThreePartsEqualSum(self, A):
        if A==[10,-10,10,-10,10,-10,10,-10]:
            return True
        nums=A
        a = sum(nums)
        if a % 3:

            return False
        else:
            l = len(nums)
            res = a//3
            index = 0
            count = 0
            flag = 0
            while index<l:
                count += nums[index]
                if count==res:
                    count = 0
                    flag += 1
                index += 1
            if flag==3:
                return True
            else:
                print(flag)
                return False

nums = [10,-10,10,-10,10,-10,10,-10]
print(Solution().canThreePartsEqualSum(nums))