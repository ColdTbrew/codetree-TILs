original = input()
s = list(original)
summ = 0
for i in s:
    summ += int(i)
s.reverse()
ans = ''.join(map(str, s))
print(ans, summ)