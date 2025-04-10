from collections import deque

MAX_L = 70
R, C, K  = 0, 0, 0
A = [[0] * MAX_L for _ in range(MAX_L + 3)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
isExit = [[False] * MAX_L for _ in range(MAX_L + 3)]
answer = 0

def inRange(y, x):
    return 3 <= y < R + 3 and 0 <= x < C

def resetMap():
    for i in range(R+3):
        for j in range(C):
            A[i][j] = 0
            isExit[i][j] = False

def canGo(y, x):
    flag = 0<=x-1 and x+1 < C and y+1 < R+3
    flag = flag and (A[y - 1][x - 1] == 0)
    flag = flag and (A[y - 1][x] == 0)
    flag = flag and (A[y - 1][x + 1] == 0)
    flag = flag and (A[y][x - 1] == 0)
    flag = flag and (A[y][x] == 0)
    flag = flag and (A[y][x + 1] == 0)
    flag = flag and (A[y + 1][x] == 0)
    return flag

def bfs(y, x):
    result = y
    q = deque([(y, x)])
    visit = [[False] * C for _ in range(R+3)]
    visit[y][x] = True

    while q:
        cury, curx = q.popleft()
        for k in range(4):
            ny, nx = cury + dy[k] , curx + dx[k]
            if inRange(ny, nx) and not visit[ny][nx] and (A[ny][nx] == A[cury][curx] or (A[ny][nx] != 0 and isExit[cury][curx])):
                q.append((ny, nx))
                visit[ny][nx] = True
                result = max(result, ny)
    return result

def down(y, x, d, id):
    if canGo(y + 1, x):
        # 아래로 내려갈 수 있는 경우입니다
        down(y + 1, x, d, id)
    elif canGo(y + 1, x - 1):
        # 왼쪽 아래로 내려갈 수 있는 경우입니다
        down(y + 1, x - 1, (d + 3) % 4, id)
    elif canGo(y + 1, x + 1):
        # 오른쪽 아래로 내려갈 수 있는 경우입니다
        down(y + 1, x + 1, (d + 1) % 4, id)
    else:
        if not inRange(y-1, x-1) or not inRange(y+1, x+1):
            resetMap()
        else:
            A[y][x] = id
            for k in range(4):
                A[y+dy[k]][x+ dx[k]] = id
            isExit[y+dy[d]][x+dx[d]] = True
            global answer
            answer += bfs(y, x) - 3  + 1


R, C, K = map(int, input().split())
for id in range(1, K+1):
    x, d = map(int, input().split())
    down(0, x-1, d, id)
print(answer)