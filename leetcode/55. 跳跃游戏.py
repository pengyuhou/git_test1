class Solution(object):
    def canJump(self, nums):
        l = len(nums)
        if l == 1:
            return True
        max_distance = -float('inf')
        for i in range(l - 1):
            if nums[i] + i > max_distance:
                max_distance = nums[i] + i
            if max_distance <= i:
                return False
            if max_distance >= l - 1:
                return True
        return False

if __name__ == "__main__":
    print(Solution().canJump( [3,2,1,0,4]))
