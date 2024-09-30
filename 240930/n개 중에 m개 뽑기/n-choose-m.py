n, m = tuple(map(int, input().split()))
ans = []

def choose(cur_num, cnt):
    if cur_num == n+1:
        if cnt== m:
            for elem in ans:
                print(elem , end = " ")
            print()
        return
    ans.append(cur_num)
    choose(cur_num+1, cnt+1)
    ans.pop()

    choose(cur_num+1, cnt)

choose(1, 0)