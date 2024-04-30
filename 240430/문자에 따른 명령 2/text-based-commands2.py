string = input()

dx, dy = [1,0,-1,0], [0,-1,0,1]

x, y = 0, 0 
d = 3


for (ch) in string:
    if 'R' == ch:
        d = (d+1) %4
    elif 'L' == ch:
        d = (d-1) %4
    elif 'F' == ch:   #F일때 
        if d == 0:
            x += dx[0]
            y += dy[0]
        elif d == 1:
            x += dx[1]
            y += dy[1]
        elif d == 2:
            x += dx[2]
            y += dy[2]
        elif d == 3:
            x += dx[3]
            y += dy[3]
print(f"{x} {y}")