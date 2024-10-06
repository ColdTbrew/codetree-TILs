n = int(input())
a = list(map(int, input().split()))
dp = [[-1]*(4) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1, n+1):
    # 1계단 올라오는 경우
    if i >= 1:
        for j in range(1, 4):  # 1계단은 최대 3번까지 가능
            if dp[i-1][j-1] != -1:  # 이전 층에서 j-1번 1계단을 사용한 경우
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + coins[i-1])
    
    # 2계단 올라오는 경우
    if i >= 2:
        if dp[i-2][0] != -1:  # 2계단을 오르는 경우 1계단 사용 횟수는 0으로 유지
            dp[i][0] = max(dp[i][0], dp[i-2][0] + coins[i-1])


print(max(dp[n]))