a, b = map(int, input().split(' '))

mul  =1 
for num in range(a,b+1):
    mul *= num
    
print(mul)