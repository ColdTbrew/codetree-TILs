n = int(input())

ans = list()
visited = [False for _ in range(n+1)]

def choose(cur_num):
    if cur_num == n+1:
        for elem in ans:
            print(elem, end= " ")
        print()
        return
    for i in range(n, 0, -1):
        if visited[i] != True:
            visited[i] = True
            ans.append(i)

            choose(cur_num+1)
            ans.pop()
            visited[i] = False

choose(1)