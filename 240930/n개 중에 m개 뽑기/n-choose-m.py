n, m = tuple(map(int, input().split()))
ans = []

def choose(cur_num):
    if cur_num == m:
        if ans == sorted(ans):
            for x in ans:
                print(x, end=" ")
            print()
        return
    for k in range(1, n+1):
        if k not in ans:
            ans.append(k)
            choose(cur_num+1)
            ans.pop()
    
choose(0)