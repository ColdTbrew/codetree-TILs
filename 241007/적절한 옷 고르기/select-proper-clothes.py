n, m = map(int, input().split())
cloth = [list(map(int, input().split())) for _ in range(n)]
#start, end, value
# dp[i][j]: i번째 날에 j번 옷을 입었을 때의 최대 만족도
dp = [[-1] * n for _ in range(m + 1)]

for i in range(n):
    dp[1][i] = 0

# DP 테이블 채우기
for i in range(2, m + 1):
    for j in range(n):
        if cloth[j][0] <= i <= cloth[j][1]:
            for k in range(n):
                if cloth[k][0] <= i-1 <= cloth[k][1] and dp[i-1][k] != 1:
                    dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(cloth[j][2]- cloth[k][2]))

# 마지막 날의 최대 만족도를 구합니다.
result = max(dp[m])
print(result)