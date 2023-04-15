a = int(input())
b = int(input())
n = int(input())

t = (a * 60 + b) * n

print(t // 3600, (t % 3600) // 60, t % 60)
