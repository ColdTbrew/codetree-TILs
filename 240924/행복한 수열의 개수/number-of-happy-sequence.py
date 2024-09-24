size, continuous_count = map(int, input().split())
matrix = []

for i in range(size):
    row = list(map(int, input().split()))
    matrix.append(row)

total_happy = 0

# 가로 방향 체크
for i in range(size):
    max_consecutive = 1  # 연속 카운트
    current_count = 1  # 현재 연속된 원소 개수
    
    for j in range(1, size):
        if matrix[i][j] == matrix[i][j - 1]:
            current_count += 1
        else:
            current_count = 1
        
        if current_count > max_consecutive:
            max_consecutive = current_count
    
    if max_consecutive >= continuous_count:
        total_happy += 1

# 세로 방향 체크
for j in range(size):
    max_consecutive = 1
    current_count = 1
    
    for i in range(1, size):
        if matrix[i][j] == matrix[i - 1][j]:
            current_count += 1
        else:
            current_count = 1
        
        if current_count > max_consecutive:
            max_consecutive = current_count
    
    if max_consecutive >= continuous_count:
        total_happy += 1

print(total_happy)