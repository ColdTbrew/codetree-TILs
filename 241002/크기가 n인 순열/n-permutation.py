n = int(input())
visited = [False for _ in range(n+1)]
ans = list()
def choose(cur_num):
    if cur_num == n+1:
        for elem in ans:
            print(elem, end=" ")
        print()
    for i in range(1, n+1):
        if visited[i] != True:
            visited[i] = True
            ans.append(i)

            choose(cur_num+1)

            ans.pop()
            visited[i] = False


choose(1)