from collections import deque

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 3×3 격자를 시계 방향으로 회전
def rotate_90(grid, x, y):
    new_grid = [row[:] for row in grid]
    for i in range(3):
        for j in range(3):
            new_grid[x + i][y + j] = grid[x + 2 - j][y + i]
    return new_grid

# BFS로 연결된 조각 탐색
def find_artifacts(grid):
    visited = [[False] * 5 for _ in range(5)]
    total_value = 0
    to_remove = []

    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                count, cells = bfs(grid, i, j, visited)
                if count >= 3:
                    total_value += count
                    to_remove.extend(cells)

    return total_value, to_remove

# BFS 구현
def bfs(grid, x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    target = grid[x][y]
    cells = [(x, y)]
    count = 1

    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and grid[nx][ny] == target:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cells.append((nx, ny))
                count += 1

    return count, cells

# 조각 채우기
def fill_grid(grid, to_remove, wall):
    global wall_idx
    for col in range(5):
        for row in range(4, -1, -1):
            if (row, col) in to_remove:
                grid[row][col] = wall[wall_idx]
                wall_idx += 1

# 메인 탐사 로직
def explore(grid, wall):
    max_value = 0
    best_grid = None
    best_angle = 360
    best_pos = (5, 5)

    # 모든 3×3 격자 위치와 회전 각도 탐색
    for x in range(3):
        for y in range(3):
            for angle in [90, 180, 270]:
                temp_grid = [row[:] for row in grid]
                for _ in range(angle // 90):
                    temp_grid = rotate_90(temp_grid, x, y)
                value, _ = find_artifacts(temp_grid)
                if (value > max_value or 
                    (value == max_value and angle < best_angle) or 
                    (value == max_value and angle == best_angle and (y < best_pos[1] or (y == best_pos[1] and x < best_pos[0])))):
                    max_value = value
                    best_grid = temp_grid
                    best_angle = angle
                    best_pos = (x, y)

    return max_value, best_grid

# 입력 처리
K, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(5)]
wall = list(map(int, input().split()))
wall_idx = 0

# K턴 탐사 진행
for turn in range(K):
    total_value, new_grid = explore(grid, wall)
    if total_value == 0:  # 유물 획득 불가능 시 종료
        break

    grid = new_grid
    turn_value = 0

    # 연쇄 획득
    while True:
        value, to_remove = find_artifacts(grid)
        if value == 0:
            break
        turn_value += value
        fill_grid(grid, to_remove, wall)

    print(turn_value, end=" ")