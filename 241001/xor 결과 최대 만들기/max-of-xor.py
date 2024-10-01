n, m = tuple(map(int, input().split()))
li = list(map(int, input().split()))
visited = [False for _ in range(n)]
max_res = 0

ans = list()
def choose(cur_num, cnt):
    global max_res
    if cnt == m: #3개를 골랏을때 xor의 최대값을 연산하고 max갱신
        val = 0
        for i in range(n):
            if visited[i]:
                val ^= li[i]
        max_res = max(max_res, val)
        return
    if cur_num == n:
        return
    
    choose(cur_num+1, cnt)

    visited[cur_num] = True
    choose(cur_num+1, cnt+1)
    visited[cur_num] = False
choose(0,0)
print(max_res)