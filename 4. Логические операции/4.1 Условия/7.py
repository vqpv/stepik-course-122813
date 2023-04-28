n1, n2, n3, n4 = [int(i) for i in input().split('.')]

summa = n1 + n2 + n3 + n4

if summa in (0, 255 * 4):
    result = False
elif n1 in range(0, 256) and n2 in range(0, 256) and n3 in range(0, 256) and n4 in range(0, 256):
    result = True
else:
    result = False

print(result)
