from collections import deque
#k개의 시작 지점으로 부터 방문이 가능한 서로 다른 칸수를 출력

n, k = list(map(int, input().split()))
mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

visited = [[False]* n for _ in range(n)]


starting_pos = []
for _ in range(k):
    x, y = list(map(int, input().split()))
    starting_pos.append((x-1,y-1))

def cango(x, y):
    return 0<=x < n and 0<= y < n and mat[x][y] == 0 and not visited[x][y]

q = deque()
total = 1
def bfs():
    global total
    dxs, dys = [-1, 1, 0, 0] , [0, 0, -1, 1]
    while q:
        curx, cury = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = dx+curx, dy+cury
            if cango(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))
                total += 1



for x, y in starting_pos:
    visited[x][y] = True
    q.append((x, y))
    bfs()

print(total)