nums = input().split()
c = input().split()

while c[0] != "end":
    if c[0] == "insert":
        nums.append(c[1])
        nums.sort(key=int)
    elif c[0] == "pop":
        print(nums.pop(-1))
    c = input().split()
