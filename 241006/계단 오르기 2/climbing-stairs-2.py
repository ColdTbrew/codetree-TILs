n = int(input())
a = list(map(int, input().split()))
dp = [[-1]*(4) for _ in range(n+1)]
dp[0][0] = 0
for i in range(1, n+1):
    dp[i][0] = dp[i-1][0]
    for j in range(4):
        if j>0 and i > 1:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + a[i-1])
        if i > 2:
            dp[i][j] = max(dp[i][j], dp[i-2][j] + a[i-1])  # i-2에서 2계단 오름


print(max(dp[n]))