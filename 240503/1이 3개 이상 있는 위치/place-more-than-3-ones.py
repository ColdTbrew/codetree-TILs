n = int(input())


#2차원 배열 입력받고
a = [[0]* (n+1)]
for _ in range(n):
    a.append([0] + list(map(int, input().split())))

#dx, dy  = 행, 열
dxs = [0,1,0,-1] 
dyx = [1, 0, -1, 0]

#범위 검사 함수
def in_range(x, y):
    if x <= n and x >= 1 and y <= n and y >= 1:
        return True
    else:
        return False

def sim(x,y):
    count = 0
    for dx, dy in zip(dxs, dyx):
        newx = x + dx
        newy = y + dy
        if in_range(newx, newy) and a[newx][newy] == 1:
            count += 1

    return count>=3

ans = 0
for i in range(1, n+1):
    for j in range(1,n+1):
        if sim(i,j):
            ans += 1

print(ans)