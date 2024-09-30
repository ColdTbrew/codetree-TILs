#점수를 최대로하려먼 다 시도해보고 최대인점을 남기는건데
n, m, k = map(int, input().split())
#턴의 수, 판의 값, 말의 수

#턴마다의 거리 
distances = list(map(int, input().split()))

#k개의 말의 위치 이 값이 m이랑 같아지면 점수를 얻음
pos = [1]*k 

ans = []
maxscore = 0

def choose(cur_turn, score):
    global maxscore
    if cur_turn == n:
        #턴이 끝나면
        maxscore = max(maxscore, score)
        return
    for i in range(k):
        original_pos = pos[i]
        if pos[i] < m:
            pos[i] += distances[cur_turn]
            if pos[i] >= m:
                pos[i] = m
                choose(cur_turn+1, score+1)
            else:
                choose(cur_turn+1, score)
            pos[i] = original_pos


choose(0,0)
print(maxscore)