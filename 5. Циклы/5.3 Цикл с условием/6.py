a = input().split()

num = 0

while a[0] != "exit":
    if a[0] == "zero":
        num = 0
    elif a[0] == "add":
        num += int(a[1])
    elif a[0] == "minus":
        num -= int(a[1])
    elif a[0] == "mul":
        num *= int(a[1])
    elif a[0] == "div":
        num //= int(a[1])
    elif a[0] == "result":
        print(num)
    a = input().split()
