class Solution(object):
    def exchange(self, nums):

        ret = []
        index = 0
        for i in range(len(nums)):
            if nums[i] % 2:
                ret.insert(index, nums[i])
                index += 1
            else:
                ret.append(nums[i])
        return ret

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(Solution().exchange(nums))










