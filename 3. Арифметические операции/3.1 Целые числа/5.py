a = int(input())
y = int(input())
x = int(input())
b = int(input())

a_1 = int((a - x - b) * (1 + y / 100))
a_2 = int((a_1 - b) * (1 + y / 100))
a_3 = int((a_2 - b) * (1 + y / 100))

print(a_1)
print(a_2)
print(a_3)
