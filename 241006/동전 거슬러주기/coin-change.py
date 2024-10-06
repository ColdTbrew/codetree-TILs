# dp[i] = max(dp[i], dp[i- coin[j]] + 1 )

n, m = tuple(map(int, input().split()))
coin = list(map(int, input().split()))
dp = [10000] * (m+1)
dp[0] = 0
for i in range(1, m+1):
    for j in range(n):
        if i >= coin[j]:
            if dp[i- coin[j]] == -1:
                continue # i 번째 칸으로 점프 못함
            dp[i] = min(dp[i] , dp[i-coin[j]]+ 1)



print(dp[m])