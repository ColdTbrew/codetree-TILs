mode,rap  = input().split(' ')
rap = int(rap)

if mode == 'A':
    num = 1
    for i in range(rap):
        print(num, end= ' ')
        num +=1
else:
    num = rap
    for i in range(rap):
        print(num, end= ' ')
        num -=1