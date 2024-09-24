n, t = map(int, input().split())
belt = []
for i in range(2):
    row = list(map(int, input().split()))
    belt.append(row)

for time in range(t):
    temp1 = belt[0][n-1]
    for i in range(n-1, 0, -1):
        belt[0][i] = belt[0][i-1]
    belt[0][0] = belt[1][n-1]

    for i in range(n-1, 0, -1):
        belt[1][i] = belt[1][i-1]
    belt[1][0] = temp1

for row in belt:
    for x in row:
        print(x, end=" ")
    print("")