a = {int(i) for i in input().split()}

res = sum(map(lambda x: x ** 2, a))

print(res)
