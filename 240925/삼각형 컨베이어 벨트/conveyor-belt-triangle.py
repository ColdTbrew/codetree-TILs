n, t = list(map(int, input().split()))

belt = []

for i in range(3):
    row = list(map(int, input().split()))
    belt.append(row)

flatten_belt = []
for i in range(3):
    for j in range(n):
        flatten_belt.append(belt[i][j])


def rotation():
    temp = flatten_belt[n*3-1]
    for i in range(n*3-1, 0, -1):
        flatten_belt[i] = flatten_belt[i-1] 
    flatten_belt[0] = temp
# print("before")
# for i in range(n*n):
#     print(flatten_belt[i])

for rot in range(t):
    rotation()
# print("after")
# for i in range(n*n):
#     print(flatten_belt[i])

#printing
count = 0
for i in range(3):
    for j in range(n):
        print(flatten_belt[count], end=' ')
        count+= 1
    print()