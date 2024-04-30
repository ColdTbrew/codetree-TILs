i = int(input())
x, y = 0,0
dx, dy = [1, 0, -1, 0],[0, -1, 0, 1]
for e in range(i):
    li = input().split(' ')
    d = li[0]
    size = int(li[1])
    for k in range(size):
        if d =='E':
            x += dx[0]
            y += dy[0]
        elif d == 'S':
            x += dx[1]
            y += dy[1]
        elif d == 'W':
            x += dx[2]
            y += dy[2]    
        else:
            x += dx[3]
            y += dy[3]

print(f"{x} {y}")