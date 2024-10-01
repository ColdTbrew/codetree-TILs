n, m = tuple(map(int, input().split()))
li = list(map(int, input().split()))

max_res = 0

ans = list()
def choose(cur_num):
    global max_res
    if cur_num == n+1:
        a = ans[0]
        for r in ans:
            a ^= r
        max_res = max(max_res, a)
        return
    for elem in li:
        ans.append(elem)
        choose(cur_num+1)
        ans.pop()

choose(1)
print(max_res)