n = int(input())

mat = []
is_valid = []
result_mat = []
for i in range(n):
    row = list(map(int, input().split()))
    mat.append(row)
    empty_row = [0]*n
    full_row = [1]*n
    is_valid.append(full_row)
    result_mat.append(empty_row)

row, col = list(map(int, input().split()))

def pop(row, col): #2,3
    row = row -1
    col = col -1
    pop_reach = mat[row][col]
    mat[row][col] = 0
    for dx in range(1, pop_reach):
        new_dx = dx + row
        new_dy = col
        if new_dx >= 0 and new_dx < n and new_dy >= 0 and new_dy < n:
            mat[new_dx][new_dy] = 0
    for dx in range(1, pop_reach):
        new_dx = -dx + row
        new_dy = col
        if new_dx >= 0 and new_dx < n and new_dy >= 0 and new_dy < n:
            mat[new_dx][new_dy] = 0
    for dy in range(1, pop_reach):
        new_dx = row
        new_dy = dy + col
        if new_dx >= 0 and new_dx < n and new_dy >= 0 and new_dy < n:
            mat[new_dx][new_dy] = 0
    for dy in range(1, pop_reach):
        new_dx = row
        new_dy = -dy + col
        if new_dx >= 0 and new_dx < n and new_dy >= 0 and new_dy < n:
            mat[new_dx][new_dy] = 0


def reorder():
    for j in range(n):
        copy_i = n-1 #3, 0 
        for i in range(n-1, -1, -1):
            if mat[i][j] != 0:
                result_mat[copy_i][j] = mat[i][j]
                copy_i -= 1



pop(row, col)
# for i in range(n):
#     for j in range(n):
#         print(mat[i][j], end = " ")
#     print()

reorder()

for i in range(n):
    for j in range(n):
        print(result_mat[i][j], end = " ")
    print()