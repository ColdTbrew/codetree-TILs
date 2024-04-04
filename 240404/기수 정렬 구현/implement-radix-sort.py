from collections import deque

def radix_sort(nums):
    max_num = max(nums)
    digit = 0
    while max_num >= 10 ** digit:
        buckets =[deque() for _ in range(10)]
        for num in nums:
            digit_value = (num % (10**(digit+1))) // (10**digit)
            buckets[digit_value].append(num)
        new_nums = []
        for bucket in buckets:
            new_nums.extend(bucket)

        digit += 1

    return new_nums

n = int(input())
nums = list(map(int, input().split()))

sorted_nums = radix_sort(nums)
print(*sorted_nums)