class Solution:
    def dominantIndex(self, nums) -> int:
        a=nums.copy()
        a.sort()
        if len(a)==1:
            return 0
        if a[-1]>=2*a[-2]:
            return nums.index(a[-1])
        else:
            return -1






if __name__ == "__main__":
    nums = [1]
    print(Solution().dominantIndex(nums))





