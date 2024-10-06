n = int(input())
li = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if li[j] < li[i]: # i자리의 전에 해당하는 부분에 값이 더 작다면 dp 갱신
            dp[i] = max(dp[i], dp[j] + 1)

ans = -1
for elem in dp:
    ans = max(ans, elem)
print(ans)