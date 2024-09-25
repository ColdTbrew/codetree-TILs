visited = []

dys = [0, 0, -1, 1]
dxs = [-1, 1, 0, 0]
cur_x, cur_y = 0, 0
#1, 1

def in_range(x,y):
    if x < n and x >= 0 and y < n and y >= 0:
        return True
    else:
        return False


def move2bigger(r, c):
    visited.append(mat[r][c])  # 시작 위치의 값 기록
    while True:
        big_exist = False  # 더 큰 값이 있는지 확인하는 변수
        for dx, dy in zip(dxs, dys):  # 상하좌우 탐색
            new_x, new_y = r + dx, c + dy
            if in_range(new_x, new_y):  # 새로운 좌표가 범위 내인지 확인
                if mat[new_x][new_y] > mat[r][c]:  # 더 큰 값이 있으면
                    r, c = new_x, new_y  # 새로운 좌표로 이동
                    visited.append(mat[r][c])  # 새로운 위치의 값 기록
                    big_exist = True  # 더 큰 값이 있었음을 표시
                    break  # 새로운 위치에서 다시 탐색
        if not big_exist:  # 더 큰 값이 없으면 종료
            break


n, r, c = list(map(int, input().split()))

mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)



move2bigger(r-1, c-1)
for x in visited:
    print(x, end= " ")