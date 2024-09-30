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
    choose(cur_num+1, cnt+1) #컬넘 자리의 숫자를 사용한 경우, 선택을 하면 카운트를 올리고
    ans.pop()

    choose(cur_num+1, cnt) #컬넘 자리의 숫자를 사용하지 않았을때

choose(1, 0)