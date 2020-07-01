num, v = map(int, input().split())
goods = []
for i in range(num):
    goods.append([int(i) for i in input().split()])

dp = [[0 for _ in range(v + 1)] for _ in range(num + 1)]
print(dp)

for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        dp[i][j] = dp[i - 1][j]
        if j - goods[i - 1][0] >= 0:
            dp[i][j] = max(dp[i][j],dp[i-1][j - goods[i - 1][0]]+goods[i-1][1] )
