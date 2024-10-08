n = int(input())

# topdown 메모이제이션
memo = [-1 for _ in range(n+1)]
# def fibo(x):
#     if memo[x] != -1:
#         return memo[x]
#     if x <= 2:
#         memo[x] = 1
#     else:
#         memo[x] = fibo(x-1)+fibo(x-2)
#     return memo[x]

# print(fibo(n))

# bottom up tabulation
f = [-1 for _ in range(n+1)]
if n<= 2:
    print(1)
else:
    f[1] = 1
    f[2] = 1
    for i in range(3, n+1):
        f[i] = f[i-1]+f[i-2]
    print(f[n])