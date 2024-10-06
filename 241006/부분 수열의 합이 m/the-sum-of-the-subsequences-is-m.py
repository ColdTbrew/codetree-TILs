n, m = list(map(int, input().split()))
li = list(map(int, input().split()))
dp = [10001] * (m+1)
dp[0] = 0
for i in range(0, n):
    for j in range(m, -1 , -1):
        if j>= li[i]:
            dp[j] = min(dp[j], dp[j-li[i]]+1)

if dp[m]== 10001:
    print(-1)
else:
    print(dp[m])