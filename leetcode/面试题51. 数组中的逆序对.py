class Solution(object):
    def __init__(self):
        self.count = 0

    def reversePairs(self, a):
        def dfs(nums):
            if len(nums) == 1:
                return nums
            mid = len(nums) // 2
            ret = []
            left = dfs(nums[:mid])
            right = dfs(nums[mid:])
            index1 = 0
            index2 = 0
            while index1 < len(left) and index2 < len(right):
                if left[index1] <= right[index2]:
                    ret.append(left[index1])
                    index1 += 1
                else:
                    self.count += len(left) - index1
                    ret.append(right[index2])
                    index2 += 1
            ret += left[index1:]
            ret += right[index2:]
            return ret

        dfs(a)
        return self.count


if __name__ == "__main__":
    nums = [7, 5, 6, 4]
    print(Solution().reversePairs(nums))
