n1, n2, n3, n4 = [int(i) for i in input().split('.')]

result = False

if not(n1 in range(0, 256) and n2 in range(0, 256) and n3 in range(0, 256) and n4 in range(0, 256)):
    print(result)
    exit(0)
else:
    b = '{0:08b}'.format(n1) + '{0:08b}'.format(n2) + '{0:08b}'.format(n3) + '{0:08b}'.format(n4)
    b1, b2 = "", ""
    for i in b:
        if i != "1":
            break
        b1 += i
    for j in b[::-1]:
        if j != "0":
            break
        b2 += j
    if b == b1 + b2:
        result = True
    print(result)
