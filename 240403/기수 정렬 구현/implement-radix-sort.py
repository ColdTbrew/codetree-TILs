from collections import deque

def radix_sort(nums):
    max_num = max(nums)
    digit = 0
    while max_num >= 10 ** digit:
        buckets = [deque() for _ in range(10)]
        
        # 각 자릿수에 해당하는 숫자를 버킷에 분배
        for num in nums:
            digit_value = (num // (10 ** digit)) % 10
            buckets[digit_value].append(num)
        
        # 버킷에서 숫자를 꺼내어 정렬된 리스트로 만듦
        nums = []
        for bucket in buckets:
            nums.extend(bucket)
        
        digit += 1
    
    return nums

n = int(input())
nums = list(map(int, input().split()))

sorted_nums = radix_sort(nums)
print(*sorted_nums)