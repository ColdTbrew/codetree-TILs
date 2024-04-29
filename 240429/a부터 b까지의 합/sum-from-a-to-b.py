a,b = map(int, input().split(' '))


sum = 0
for num in range(a, b+1):
    sum += num

print(sum)