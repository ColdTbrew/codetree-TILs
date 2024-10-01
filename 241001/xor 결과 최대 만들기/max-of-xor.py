n, m = tuple(map(int, input().split()))
li = list(map(int, input().split()))

max_res = 0

ans = list()
def choose(cur_num, start_idx):
    global max_res
    if cur_num == m:
        a = 0  # XOR 초기값은 0이어야 함
        for r in ans:
            a ^= r
        max_res = max(max_res, a)
        return
    for i in range(start_idx, len(li)):  # start_idx를 이용하여 중복 선택 방지
        ans.append(li[i])
        choose(cur_num+1, i+1)  # i+1을 넘겨서 중복 선택을 방지
        ans.pop()

choose(0)
print(max_res)