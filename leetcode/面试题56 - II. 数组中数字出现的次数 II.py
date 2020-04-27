class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a={}
        for num in nums:
            if num not in a.keys():
                a[num]=1
            else:
                a[num] += 1
        for i,j in a.items():
            if j==1:
                return i


if __name__ == "__main__":
    nums = [9, 1, 7, 9, 7, 9, 7]
    print(Solution().singleNumber(nums))