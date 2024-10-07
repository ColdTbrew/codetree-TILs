#만약 자신의 카드가 상대방의 카드보다 작다면, 그 카드에 적혀있는 점수만큼 점수를 얻고 카드의 번호가 작은 사람의 카드를 버립니다. 
n = int(input())
ops = list(map(int, input().split())) 
me = list(map(int, input().split())) 
dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]

dp[0][0] = 0
for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            continue
        if ops[i] < me[j]:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if me[j] < ops[i]:
            dp[i][j+1] = max(dp[i][j+1] , dp[i][j]+me[j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])
ans = 0
for i in range(n+1):
    ans = max(ans, dp[n][i])
    ans = max(ans, dp[i][n])

print(ans)