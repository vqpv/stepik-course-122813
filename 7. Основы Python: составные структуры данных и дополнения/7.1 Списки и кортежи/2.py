nums = list(map(int, input().split()))

for i in range(1, len(nums)):
    print(nums[i] + nums[i - 1], end=" ")
