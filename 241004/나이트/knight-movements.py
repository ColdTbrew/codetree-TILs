directions = [
    (1, -2), (2, -1),(2, 1),(1, +2),
    (2, -1),(1, -2),(-2, -1),(-1, -2),
]
n = int(input())
pos = list(map(int, input().split()))
start = (pos[0]-1, pos[1]-1)
end = (pos[2]-1, pos[3]-1)

visited = [[False] * n for _ in range(n)]
step = [[0] * n for _ in range(n)]

from collections import deque

q = deque()

def cango(x, y):
    return 0<=x<n and 0<=y < n and not visited[x][y]
def bfs():
    while q:
        curx, cury = q.popleft()
        for dx, dy in directions:
            x = dx+curx
            y = dy + cury
            if cango(x, y):
                visited[x][y] = True
                step[x][y] = step[curx][cury] + 1
                q.append((x, y))
                if (x,y) == end or (x, y)== start:
                    return True
    return False

# BFS 시작
q.append(start)
visited[start[0]][start[1]] = True

if bfs():
    print(step[end[0]][end[1]])
else:
    print(-1)