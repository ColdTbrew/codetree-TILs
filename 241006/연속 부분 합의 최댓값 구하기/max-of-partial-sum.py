#dp[i]=max(dp[i−1]+a[i],2a[i])
# 마지막 원소가 i라 했을때 얻을 수 있는 최대 점수
# 이전 dp값 + a[i](새로운 연속부분 더하기) , 현재a[i]값의 2배 중 큰 값을 dp[i]에 넣을 거임

n = int(input())
mat = list(map(int, input().split()))
dp = [-1001]*n
dp[0] = mat[0]
for i in range(1, n):
    dp[i] = max(dp[i-1] + mat[i], mat[i])

print(dp[n])