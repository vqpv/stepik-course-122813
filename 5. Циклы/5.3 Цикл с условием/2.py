num = int(input())

result = 0

while num:
    result = result * 10 + num % 10
    num //= 10

print(result)
