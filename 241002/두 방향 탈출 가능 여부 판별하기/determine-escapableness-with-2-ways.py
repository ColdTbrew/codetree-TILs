#각 행에 뱀이 없는 경우 1, 뱀이 있는 경우 0 
# 1인 곳만 갈 수 있음
n, m = tuple(map(int, input().split()))
start = (0,0)
end = (n-1,m-1)
suc = False
visited = [[False]*m for _ in range(n)]
mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)


def cango(x, y):
    return 0 <= x < n and 0 <= y < m and mat[x][y] == 1 and not visited[x][y]

def dfs(x, y):
    global suc
    dxs = [1, 0]
    dys = [0, 1]
    for dx, dy in zip(dxs, dys):
        newx , newy = dx + x, dy+ y
        if cango(newx, newy):
            visited[newx][newy] = True
            if (newx, newy) == end:
                suc = True
            dfs(newx, newy)


dfs(0,0)
if suc:
    print(1)
else:
    print(0)