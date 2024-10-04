ans = -1
n= int(input())

f = [[-1] for _ in range(10000)]
f[1] = 0
f[2] = 1
f[3] = 1
f[4] = 1
f[5] = 2
for i in range(6, n+1):
    f[i] = f[i-3] + f[i-2]

if f[n]:
    print(f[n]%10007)
else:
    print(0)