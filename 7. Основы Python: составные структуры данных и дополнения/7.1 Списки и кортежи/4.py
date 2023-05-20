nums = map(int, input().split())

print(*sorted(nums, key=lambda x: x == 0))
