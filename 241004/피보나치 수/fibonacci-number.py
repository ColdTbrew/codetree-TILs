n = int(input())

# topdown 메모이제이션
memo = [-1 for _ in range(n)]
def fibo(x):
    if memo[x] != -1:
        return memo[x]
    if x <= 2:
        memo[x] = 1
    else:
        memo[x] = fibo(x-1)+fibo(x-2)
    return memo[x]

print(fibo(n-1))