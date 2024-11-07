def is_one_bit_diff(x, y):
    """ 두 숫자 x와 y가 이진수에서 한 비트만 다른지 확인 """
    return bin(x ^ y).count('1') == 1

# 입력 받기
a = input().strip()  # 2진법 입력
b = input().strip()  # 3진법 입력

# a와 b의 길이를 고려하여 최대 N을 설정합니다.
max_value = 1_000_000_000

# 가능한 N을 찾기 위해 0부터 max_value까지 검사
for N in range(max_value + 1):
    # N을 2진법과 3진법으로 변환
    binary_N = bin(N)[2:]  # 2진법 문자열 (앞의 '0b' 제거)
    ternary_N = ''
    
    temp = N
    while temp > 0:
        ternary_N = str(temp % 3) + ternary_N
        temp //= 3
    if not ternary_N:  # N이 0일 경우
        ternary_N = '0'
    
    # 2진법과 3진법에서 각각 a, b와 정확히 한 비트만 다르면
    if len(binary_N) == len(a) and len(ternary_N) == len(b):
        if is_one_bit_diff(int(binary_N, 2), int(a, 2)) and is_one_bit_diff(int(ternary_N, 3), int(b, 3)):
            print(N)
            break  # 유효한 N을 찾으면 종료