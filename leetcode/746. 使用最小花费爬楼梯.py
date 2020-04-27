class Solution(object):
    def minCostClimbingStairs(self, cost):
        if len(cost)==1 or cost==[]:
            return 0
        dp = [0 for _ in range(len(cost)+1)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        l = len(cost) + 1
        for i in range(l):
            if i==0 or i==1:
                continue
            if i==l-1:
                dp[i] = min(dp[i-1],dp[i-2])
            else:
                dp[i] = min(dp[i-1]+cost[i],dp[i-2]+cost[i])
        return dp[-1]


if __name__ == "__main__":
    cost = [1]
    print(Solution().minCostClimbingStairs(cost))