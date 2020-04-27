class Solution(object):
    def canThreePartsEqualSum(self, A):
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
                return False


if __name__ == "__main__":
    nums = [0,2,1,-6,6,-7,9,1,2,0,1]
    print(Solution().canThreePartsEqualSum(nums))





