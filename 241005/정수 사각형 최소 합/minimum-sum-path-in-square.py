n = int(input())
mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

# DP 테이블 초기화
dp = [[0]*n for _ in range(n)]

# 시작점 초기화 (1, N) -> (0, n-1)
dp[0][n-1] = mat[0][n-1]

# 첫 번째 행과 마지막 열 초기화
for i in range(n-2, -1, -1):
    dp[0][i] = dp[0][i+1] + mat[0][i]  # 첫 번째 행
    dp[i][n-1] = dp[i+1][n-1] + mat[i][n-1]  # 마지막 열

# DP 테이블 채우기
for i in range(1, n):
    for j in range(n-2, -1, -1):
        dp[i][j] = min(dp[i-1][j], dp[i][j+1]) + mat[i][j]

# 결과 출력 (N, 1) -> (n-1, 0)
print(dp[n-1][0])