arr = list(map(int, input().split()))
a = arr[0]
b = arr[1]

m = a if a > b else b

print(m)