# 상하좌우 방향 순서대로 우선순위를 매겨 가능한 곳 
n, curr_x, curr_y = map(int, input().split())
a = [[0]* (n+1)]
for _ in range(n):
    a.append([0] + list(map(int, input().split())))

visited_nums = []

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

def can_go(x, y, curr_num):
    return in_range(x,y) and a[x][y] > curr_num

def sim():
    global curr_x, curr_y

    dx, dy = [-1, 1, 0, 0], [0,0,-1,1]
    for x, y in zip(dx,dy):
        new_x , new_y = curr_x + x, curr_y+y

        if can_go(new_x,new_y, a[curr_x][curr_y]):
            curr_x, curr_y = new_x, new_y
            return True


    return False

visited_nums.append(a[curr_x][curr_y])

while True:
    greater_number_exist = sim()

    if not greater_number_exist:
        break

    visited_nums.append(a[curr_x][curr_y])

for num in visited_nums:
    print(num, end= ' ')