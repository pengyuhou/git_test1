class Solution(object):
    def canPartition(self, nums):
        res = sum(nums) / 2
        if res == int(res):
            mark = [False for _ in range(len(nums))]
            nums.sort()
            nums.reverse()
            if nums[0] > sum(nums[1:]):
                return False

            def dfs(ret):
                if sum(ret) >= res:
                    if res == 0:
                        return True
                    if sum(ret) == res:
                        return True
                    return False
                for i in range(len(nums)):
                    if not mark[i]:
                        mark[i] = not mark[i]
                        ret.append(nums[i])
                        a = dfs(ret)
                        ret.pop()
                        mark[i] = not mark[i]
                        if a:
                            return True
                return False

            return dfs([])
        else:
            return False


if __name__ == "__main__":
    a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100]
    print(Solution().canPartition(a))
