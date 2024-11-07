original = input()  # 사용자 입력
s = list(original)  # 입력된 문자열을 리스트로 변환
summ = 0  # 합계를 저장할 변수 초기화

# 각 문자에 대해 정수로 변환하여 합계 계산
for i in s:  # s에서 반복
    summ += int(i)

s.reverse()  # 리스트를 반대로 뒤집음
ans = ''.join(s)  # 뒤집힌 리스트를 문자열로 변환

# 결과 출력
print(ans, summ)