import bisect

nums = []

s = input()

while s != "change":
    bisect.insort(nums, int(s))
    s = input()

s = input() 

while s != "close":
    print(bisect.bisect_right(nums, int(s)) - 1)
    s = input()
