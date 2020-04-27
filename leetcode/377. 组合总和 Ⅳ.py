# 深搜超时
class Solution(object):
    def __init__(self):
        self.count = 0
    def combinationSum4(self, nums, target):
        def dfs(p, res):
            if sum(res) >= target:
                if sum(res) == target:
                    self.count += 1
                return
            for i in range(len(p)):
                res.append(p[i])
                dfs(p, res)
                res.pop()
        dfs(nums,[])
        return self.count

"""
本题为动态规划的背包问题
"""
class Solution1(object):
    def combinationSum4(self, nums, target):
        dp = [0 for _ in range(target+1)]
        for num in nums:
            if num<=target:
                dp[num] = 1
        for i in range(len(dp)):
            for num in nums:
                if i-num>=0:
                    dp[i] += dp[i-num]
        return dp[-1]






if __name__ == "__main__":
    nums = [9]
    target = 3
    print(Solution1().combinationSum4(nums, target))
