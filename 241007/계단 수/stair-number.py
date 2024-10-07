n = int(input())
dp = [[0]*10 for _ in range(n+1)]

for digit in range(1, 10):
    dp[1][digit] = 1

for length in range(2, n+1):
    for digit in range(10):
        if digit > 0:
            dp[length][digit] += dp[length-1][digit-1]
        if digit < 9:
            dp[length][digit] += dp[length-1][digit+1]
        dp[length][digit] %= (10**9 + 7)

print(sum(dp[n]) %(10**9 + 7))