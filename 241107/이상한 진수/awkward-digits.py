# 입력 받기
a = input().strip()
b = input().strip()

# a로부터 가능한 N 생성 (2진수)
possible_from_a = []
for i in range(len(a)):
    # 현재 비트를 반전
    flipped_bit = '1' if a[i] == '0' else '0'
    # 새로운 이진수 문자열 생성
    new_a = a[:i] + flipped_bit + a[i+1:]
    # 정수로 변환하여 리스트에 추가
    possible_from_a.append(int(new_a, 2))

# b로부터 가능한 N 생성 (3진수)
possible_from_b = []
for i in range(len(b)):
    # 현재 자리의 숫자를 제외한 나머지 두 숫자로 변경
    for digit in '012':
        if b[i] != digit:
            new_b = b[:i] + digit + b[i+1:]
            possible_from_b.append(int(new_b, 3))

# 가능한 N들의 교집합 찾기
possible_N = set(possible_from_a) & set(possible_from_b)

# 결과 출력
print(possible_N.pop())