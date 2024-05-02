n = int(input())
arr = []
for i in range(n):
    k = int(input())
    arr.append(k)

s1 , e1 = map(int,input().split())
s2 , e2 = map(int,input().split())

# s1, e1, s2, e2 값을 0부터 시작하는 인덱스로 변환
s1 = s1 - 1
s2 = s2 - 1

# 첫 번째 블록 제거
temp = arr[:s1] + arr[e1:]

# 두 번째 블록 제거
arr = temp[:s2] + temp[e2:]

# 남은 블록 개수 출력
print(len(arr))

# 남은 블록 출력
for i in range(len(arr)):
    print(arr[i])