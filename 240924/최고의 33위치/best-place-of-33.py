size = int(input())
matrix = [[0 for w in range(size)] for h in range(size)]

for i in range(size):
    matrix[i] = list(map(int, input().split()))

def coin_sum(i, j):
    count = 0
    for dx in range(3):
        for dy in range(3):
            if i+dx >= size or j+dy >= size:
                pass
            else:
                if matrix[i+dx][j+dy] == 1:
                    count += 1
    return count

real_max = 0

for i in range(size):
    for j in range(size):
        summ = coin_sum(i, j)
        if real_max < summ:
            real_max = summ

print(real_max)