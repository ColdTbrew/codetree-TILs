from collections import deque
n, m = tuple(map(int, input().split()))
mat = []

for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

visited = [[False] * m for _ in range(n)]
step = [[0] * m for _ in range(n)]

def cango(x, y):
    return 0<=x<n and 0<=y<m and mat[x][y]== 1 and not visited[x][y]

end = (n-1, m-1)
q = deque()
suc = False
def bfs():
    global suc
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        (curx, cury) = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = dx+curx, dy+cury
            if cango(nx, ny):
                visited[nx][ny] = True
                step[nx][ny] = step[curx][cury] + 1
                q.append((nx, ny))
                if end == (nx, ny):
                    suc = True

q.append((0,0))
visited[0][0] = True
step[0][0] = 0
bfs()

if suc:
    print(step[n-1][m-1])
else:
    print(-1)

# for i in range(n):
#     for j in range(m):
#         print(step[i][j], end = " ")
#     print()