def find_next_number():
    a, b, c = map(int, input().split())
    d = c - b
    e = b - a
    if d == e:
        print(c + d)
    else:
        print("The sequence is not an arithmetic progression.")

find_next_number()