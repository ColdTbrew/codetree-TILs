#만약 자신의 카드가 상대방의 카드보다 작다면, 그 카드에 적혀있는 점수만큼 점수를 얻고 카드의 번호가 작은 사람의 카드를 버립니다. 
n = int(input())
ops = list(map(int, input().split())) 
me = list(map(int, input().split())) 
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        # 남우의 카드가 상대방의 카드보다 작을 때
        if me[j] < ops[i]:
            dp[i][j] = max(dp[i][j], dp[i][j+1] + me[j])
        # 남우의 카드가 같거나 클 때
        else:
            # 남우의 카드를 버리는 경우
            dp[i][j] = max(dp[i][j], dp[i+1][j])
            # 상대방의 카드를 버리는 경우
            dp[i][j] = max(dp[i][j], dp[i+1][j+1])

print(dp[0][0])