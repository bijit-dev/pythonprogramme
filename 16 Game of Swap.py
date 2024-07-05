a, b = input().split()
a, b = int(a), int(b)
print("Before swapping: num1 = ", a, ", num2 = ", b)
temp = a
a = b
b = temp
print("After swapping: num1 = ", a, ", num2 = ", b)