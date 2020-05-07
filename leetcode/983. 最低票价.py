class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        res = [(1, costs[0]), (7, costs[1]), (30, costs[2])]
        dp = [float('inf') for _ in range(days[-1]+1)]
        dp[0] = 0
        for now in range(1, len(dp)):
            if now in days:
                for i, cost in res:
                    if now - i >= 0:
                        dp[now] = min(dp[now],dp[now-i]+cost)
                    else:
                        dp[now] = min(dp[now],dp[0]+cost)
            else:
                dp[now] = dp[now-1]
        return dp[-1]


if __name__ == "__main__":
    print(Solution().mincostTickets(days=[1,4,6,7,8,20], costs=[2, 7, 15]))
