class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        l = len(nums)
        ret = []
        for i in range(l - 3):
            for j in range(i + 1, l - 2):
                left = j + 1
                right = l - 1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        ret.append(sorted([nums[i], nums[j], nums[left], nums[right]]))
                        left += 1
                        right -= 1
        ret = list(map(tuple, ret))
        return list(map(list, set(ret)))


if __name__ == "__main__":
    print(Solution().fourSum([-5, 5, 4, -3, 0, 0, 4, -2],
                             4))
