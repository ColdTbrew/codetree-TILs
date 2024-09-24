n, m = map(int, input().split())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)



def check_hori(i, m):
    same = 0
    represent = matrix[i][0]
    for j in range(n):
        if represent == matrix[i][j]:
            same += 1
    if same >= m:
        return True
    else:
        return False
def check_verti(j, m):
    same = 0
    represent = matrix[0][j]
    for i in range(n):
        if represent == matrix[i][j]:
            same += 1
    if same >= m:
        return True
    else:
        return False

happy_count = 0
for i in range(n):
    if check_hori(i,m):
        happy_count += 1
    if check_verti(i,m):
        happy_count += 1

print(happy_count)