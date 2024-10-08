n, m, t = list(map(int, input().split()))
mat = []
marvels = []
next_marvels = []

for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)
    
# 각 행이 독립적인 리스트가 되도록 초기화
marvels = [[0]*n for _ in range(n)]
next_marvels = [[0]*n for _ in range(n)]

for _ in range(m):
    i, j = list(map(int, input().split()))
    marvels[i-1][j-1] = 1

# Direction arrays matching priority: Up, Down, Left, Right
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def move(i, j):
    max_value = 0
    best_x, best_y = i, j
    for d in range(4):
        newx = i + dxs[d]
        newy = j + dys[d]
        if 0 <= newx < n and 0 <= newy < n:
            cell_value = mat[newx][newy]
            if cell_value > max_value:
                max_value = cell_value
                best_x, best_y = newx, newy
    next_marvels[best_x][best_y] += 1

def handle_collisions():
    for i in range(n):
        for j in range(n):
            if next_marvels[i][j] > 1:
                next_marvels[i][j] = 0

def reflex():
    # Update marvels with the new positions
    for i in range(n):
        for j in range(n):
            marvels[i][j] = next_marvels[i][j]
    # Reset next_marvels for the next turn
    for i in range(n):
        for j in range(n):
            next_marvels[i][j] = 0

def marvel_count():
    count = 0
    for i in range(n):
        for j in range(n):
            if marvels[i][j] == 1:
                count += 1
    return count

# Time progression
for _ in range(t):
    for i in range(n):
        for j in range(n):
            if marvels[i][j] == 1:
                move(i, j)
    handle_collisions()
    reflex()

print(marvel_count())