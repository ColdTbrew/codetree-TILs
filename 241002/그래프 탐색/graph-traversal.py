#dfs를 각번호에서 돌리는데
#1번 정점에서 시작한 도달가능한 정점만 필요함
#노드개수만큼의 배열에 번호를 적어놔야함

n, m = tuple(map(int, input().split()))
mat = [[0 for _ in range(n)] for _ in range(n)]
visited = [False for _ in range(n)]
for i in range(m):
    x, y = tuple(map(int, input().split()))
    mat[x-1][y-1] = 1
    mat[y-1][x-1] = 1

count = 0
def dfs(node):
    global count
    for cur_node in range(1, n+1):
        if visited[cur_node-1] != True and mat[node-1][cur_node-1]:
            #print(cur_node)
            visited[cur_node-1] = True
            count += 1
            dfs(cur_node)



# for i in range(n):
#     for j in range(n):
#         print(mat[i][j], end = " ")
#     print()
dfs(0)
print(count)