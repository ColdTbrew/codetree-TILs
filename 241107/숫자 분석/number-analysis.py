s = list(map(int, input()))
s.reverse()
ans = ''.join(map(str, s))
summation = sum(s)

print(ans, summation)