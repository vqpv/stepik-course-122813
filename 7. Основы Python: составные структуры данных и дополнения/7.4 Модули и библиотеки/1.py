d = {}

for _ in range(int(input())):
    a, b = input().split()
    d[b] = d.get(b, [])
    d[b].append(a)

for i, j in enumerate(sorted(d.items())):
    for x in sorted(j[1]):
        print(j[0], x)
    if i != len(d) - 1:
        print("<->")
