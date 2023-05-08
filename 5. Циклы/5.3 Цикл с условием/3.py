num = int(input())

result = 0
num_2 = num

while num > 0:
    result = result * 10 + num % 10
    num //= 10

print(num_2 == result)
