n = int(input())
mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

dp = [[0]*n for _ in range(n)]

dp[0][0] = mat[0][0 ]

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + mat[i][0]
    dp[0][i] = dp[0][i-1] + mat[0][i]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + mat[i][j]

a = -1
for i in range(n):
    a = max(a, dp[n-1][i])

print(a)