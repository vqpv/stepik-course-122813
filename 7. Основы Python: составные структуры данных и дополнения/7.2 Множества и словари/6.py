s = input()

d = {}

while s != "end":
    a, b = s.split()
    d[a] = d.get(a, 0) + 1
    d[b] = d.get(b, 0) + 1
    s = input()

for i, j in sorted(d.items(), key=lambda x: x[0].lstrip("/")):
    print(i, j)
