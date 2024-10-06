n = int(input())
li  = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if li[i] < li[j]:
            dp[i] = max(dp[i] , dp[j] + 1)

ans = -1
for elem in dp:
    ans = max(ans, elem)

print(ans)

# for i in range(n-1, 0, -1):
#     for j in range(i, -1, -1):
#         if li[i] li[j]
#         dp[i] = max(dp[i[]])