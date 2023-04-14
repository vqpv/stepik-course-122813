time_mins = int(input())
start_hours = int(input())
start_mins = int(input())

m = start_hours * 60 + start_mins + time_mins

print((m // 60) % 24, m % 60)
