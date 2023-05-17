from functools import reduce

nums = map(int, input().split())

res = reduce(lambda a, b: a * b, nums)

print(res)
