s = input().split()

d = {}

for i in s:
    d[i] = d.get(i, 0) + 1

for key, res in sorted(d.items()):
    print(key, res)
