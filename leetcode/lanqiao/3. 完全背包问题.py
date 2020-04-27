num, V_total = map(int, input().split())
stuff = []
for _ in range(num):
    stuff.append(list(map(int, input().split())))

dp = [0 for _ in range(V_total+1)]
for v,w in stuff:
    for i in range(1,len(dp)):
        if i>=v:
            dp[i] = max(dp[i],dp[i-v]+w)
print(dp[-1])



