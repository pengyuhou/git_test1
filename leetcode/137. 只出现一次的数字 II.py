class Solution(object):
    def singleNumber(self, nums):
        a = {}
        for num in nums:
            if num not in a.keys():
                a[num] = 1
            else:
                a[num] += 1
        return [i for i,j in list(a.items()) if j==1][0]



if __name__ == "__main__":

    print(Solution().singleNumber([2,2,3,2]))

















