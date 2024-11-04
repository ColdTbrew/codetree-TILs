from itertools import permutations
N = int(input())
a = []
b = []
for _ in range(N):
    x  = int(input())
    a.append(x)
M = int(input())
for _ in range(M):
    x  = int(input())
    b.append(x)

ans = []

# a 리스트에서 길이가 m인 수열을 가져와서 아름다운 수열인지 검사해야함
for start_idx in range(0, N-M+1):
    # print("start_", start_idx)
    hubo = sorted(a[start_idx : start_idx+M])
    # print(hubo)
    b.sort()
    # print(b)
    subs = []
    for x, y in zip(hubo, b):
        sub = x - y
        subs.append(sub)
    if all(x == subs[0] for x in subs):
        ans.append(start_idx+1)

print(len(ans))
for a in ans:
    print(a)