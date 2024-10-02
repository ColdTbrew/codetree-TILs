from collections import deque

n, m = tuple(map(int, input().split()))
mat = []
visited = [[False] * m for _ in range(n)]

for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

def cango(x, y):
    return 0<=x< n and 0<= y < m and mat[x][y] == 1 and not visited[x][y]

q = deque()
suc = False
def bfs():
    global suc
    dxs = [-1,1, 0, 0]
    dys = [0, 0, -1, 1]
    while q:
        curx, cury = q.popleft()
        for dx, dy in zip(dxs, dys):
            newx = curx + dx
            newy = cury + dy
            if cango(newx, newy):
                visited[newx][newy] = True
                q.append((newx, newy))
                if (newx, newy) == (n-1, m-1):
                    suc = True


q.append((1,1))
bfs()
if suc:
    print(1)
else:
    print(0)