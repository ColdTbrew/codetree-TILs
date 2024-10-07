n, m = map(int, input().split())
cloth = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j]: i번째 날에 j번 옷을 입었을 때의 최대 만족도
dp = [[-1] * n for _ in range(m + 1)]

# 초기화: 가능한 첫 날의 옷들에 대해 dp 설정
for i in range(n):
    s, e, v = cloth[i]
    if s == 1:
        dp[1][i] = 0  # 첫 날에는 만족도 차이가 없으므로 0으로 설정

# DP 테이블 채우기
for day in range(2, m + 1):
    for i in range(n):
        s1, e1, v1 = cloth[i]
        if s1 <= day <= e1:  # i번 옷이 day 날에 입을 수 있는 경우
            for j in range(n):
                s2, e2, v2 = cloth[j]
                if s2 <= day - 1 <= e2 and dp[day - 1][j] != -1:
                    # 이전 날에 j번 옷을 입었고, 현재 옷을 입을 수 있는 경우
                    diff = abs(v1 - v2)
                    dp[day][i] = max(dp[day][i], dp[day - 1][j] + diff)

# 마지막 날의 최대 만족도를 구합니다.
result = max(dp[m])
print(result)