nums = sorted(map(int, input().split()))

if len(nums) % 2:
    res = nums[len(nums) // 2]
else:
    res = (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
    if res.is_integer():
        res = int(res)
    else:
        res = round(res, 1)

print(res)
