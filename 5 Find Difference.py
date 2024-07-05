a, b = input().split()
a, b = int(a), int(b)
c = a-b if a > b else b-a
print(int(c))