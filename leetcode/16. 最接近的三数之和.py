class Solution(object):
    def threeSumClosest(self, nums, target):
        l = len(nums)
        nums.sort()
        res = float('inf')
        ret = float('inf')
        for i in range(l - 2):
            left = i + 1
            right = l - 1
            while left < right:
                x = nums[left] + nums[right] + nums[i]
                if x > target:
                    if abs(x - target) < res:
                        res = abs(x - target)
                        ret = x
                    right -= 1
                elif x < target:
                    if abs(x - target) < res:
                        res = abs(x - target)
                        ret = x
                    left += 1
                else:
                    return target
        return ret


if __name__ == "__main__":
    print(Solution().threeSumClosest(nums=[-1, 2, 1, -4], target=1))
