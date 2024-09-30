#단, 연속하여 같은 숫자가 3번 이상 나오는 경우는 제외합니다.

k, n = map(int, input().split())
ans = []
def choose(cur_num):
    i = 0
    if cur_num == n+1:
        for a in ans:
            print(a, end=" ")
        print()
        return
    
    for kx in range(1, k+1):
        if len(ans) >= 2 and ans[-1] == ans[-2] == kx:
            continue
        else:
            ans.append(kx)
            choose(cur_num+1)
            ans.pop()

choose(1)