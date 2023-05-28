c = input().split()

tasks = []

while c[0] != "end":
    if c[0] == "task":
        n, p = c[1].split(",")
        tasks.append([int(n), int(p)])
        tasks.sort(key=lambda x: (x[1], x[0]))
    elif c[0] == "take":
        print("Задача", tasks[-1][0], "с приоритетом", tasks[-1][1])
        tasks.pop(-1)
    c = input().split()
