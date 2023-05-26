c = input().split()

nums = []

while c[0] != "close":
    if c[0] == "add":
        nums.append(c[1])
    elif c[0] == "pop":
        print(nums.pop())
    elif c[0] == "head":
        print(nums[-1])
    c = input().split()
