#i, j를 모두 돌며 dfs를 실행하는데 각 dfs마다 사람수를 저장해두고   
#dfs가 시작된 위치의 개수를 세면 마을 수를 알수 있음

n = int(input())
mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)
visited = [[0]*n for _ in range(n)]
total_village_cnt = 0
populations = []

def cango(x, y):
    if 0<= x < n and 0<= y <n and mat[x][y] == 1 and not visited[x][y]:
        return True
    else:
        return False


def dfs(x, y):
    global people
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        newx, newy = dx + x, dy+ y
        if cango(newx, newy):
            visited[newx][newy] = True
            people += 1
            dfs(newx, newy)
    



for i in range(n):
    for j in range(n):
        if visited[i][j] != True and mat[i][j] == 1:
            total_village_cnt += 1
            people = 1
            visited[i][i] = True
            dfs(i, j)
            populations.append(people)


print(total_village_cnt)
for p in sorted(populations):
    print(p)