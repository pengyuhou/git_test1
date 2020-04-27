class Solution(object):
    def singleNumbers(self, nums):
        a = {}
        for num in nums:
            if num not in a.keys():
                a[num]=1
            else:
                a[num] += 1
        ret = []
        for i,j in a.items():
            if j==1:
                ret.append(i)
        return ret


if __name__ == "__main__":
    nums = [4, 1, 4, 6]
    print(Solution().singleNumbers(nums))




