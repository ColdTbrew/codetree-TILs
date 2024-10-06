n = int(input())
li = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n): 
    for j in range(0, i): #i 의 이전에 해당하는 부분
        if li[j] < li[i]: # i자리의 전에 해당하는 부분에 값이 더 작다면 dp 갱신
            dp[i] = max(dp[i], dp[j] + 1)
#	•	li[j] < li[i]라는 조건이 만족되었을 때, dp[j] + 1이 의미하는 것은, 
# j까지의 수열에 i번째 원소를 추가함으로써 증가 부분 수열의 길이가 하나 더 늘어나는 것을 의미합니다.
ans = -1
for elem in dp:
    ans = max(ans, elem)
print(ans)