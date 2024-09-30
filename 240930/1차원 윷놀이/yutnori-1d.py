#점수를 최대로하려먼 다 시도해보고 최대인점을 남기는건데
n, m, k = map(int, input().split())
#턴의 수, 판의 값, 말의 수

#턴마다의 거리 
distances = list(map(int, input().split()))

#k개의 말의 위치 이 값이 m이랑 같아지면 점수를 얻음
pos = [1 for _ in range(k)]
maxscore = 0

def calc():
    score = 0
    for p in pos:
        score += (p >= m)
    return score

def find_max(count):
    global maxscore

    #말을 움직이지 않아도 
    #최대가 될 수 있음으로 항상 답을 갱신
    maxscore = max(maxscore, calc())

    if count == n: #턴 끝
        return
    for i in range(k):
        # if pos[i] >= m:
        #     continue
        pos[i] += distances[count] #턴에 맞는 이동 거리더하기
        find_max(count+1)
        pos[i] -= distances[count] #백트레킹

find_max(0)
print(maxscore)