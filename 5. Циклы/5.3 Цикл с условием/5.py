n1, n2, n3, n4 = [int(i) for i in input().split('.')]
m1, m2, m3, m4 = [int(i) for i in input().split('.')]

result_n = False
result_m = False

if n1 in range(0, 256) and n2 in range(0, 256) and n3 in range(0, 256) and n4 in range(0, 256) and not (n1 in (0, 255) and n1 == n2 and n1 == n3 and n1 == n4):
    result_n = True

if m1 in range(0, 256) and m2 in range(0, 256) and m3 in range(0, 256) and m4 in range(0, 256):
    b1, b2 = "", ""
    b = '{0:08b}'.format(m1) + '{0:08b}'.format(m2) + '{0:08b}'.format(m3) + '{0:08b}'.format(m4)
    for i in b:
        if i != "1":
            break
        b1 += i
    for j in b[::-1]:
        if j != "0":
            break
        b2 += j
    if b == b1 + b2:
        result_m = True

if not (result_n and result_m):
    print("Валидация не пройдена")
    exit(0)
else:
    print(n1 & m1, n2 & m2, n3 & m3, n4 & m4, sep=".")
