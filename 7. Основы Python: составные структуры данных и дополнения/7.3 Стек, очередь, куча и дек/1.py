n = input()

nums = []

while n != "-1":
    nums.append(n)
    n = input()

print(*nums[::-1], sep="\n")
