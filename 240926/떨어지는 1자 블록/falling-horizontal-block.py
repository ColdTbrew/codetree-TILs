n, m , k = list(map(int, input().split()))

mat = []

for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

dest_x = -1

block = [1]*m

start_x, start_y = 0, k-1
cur_x = 0
cur_y = 0
able = False

for dx in range(n):
#스타트 포지션 부터 블락의 길이만큼 열방향으로 탐색해서 모두0이면 dx를 다음으로 넘어가고
# 1이 하나라도 나오면 0행에 넣기
    count = 0
    for dy in range(len(block)):
        cur_x = dx
        cur_y = start_y + dy
        #print(cur_x, cur_y)
        if mat[cur_x][cur_y] == 0:
            count += 1
        else:
            count = 0
    if count == len(block):
        dest_x += 1



for dy in range(len(block)):
    # print(dest_x,start_y+dy)
    mat[dest_x][start_y+dy] = 1
# else:
#     print("not able")
#     for dy in range(len(block)):
#         mat[0][start_y+dy] = 1

for i in range(n):
    for j in range(n):
        print(mat[i][j] , end = " ")
    print()