a = str(input()) #2진법인풋
b = str(input()) #3진법 인풋

N_a = 0
N_b = 0
two = 2
for idx in range(len(str(a))):
    if a[idx]:
        N_a += 2 ** idx

for idx in range(len(str(b))):
    if b[idx]:
        N_b += 3 ** idx

print((N_a+N_b)//2)