from datetime import time, timedelta


t1 = time.fromisoformat(input())
t2 = time.fromisoformat(input())

h1 = timedelta(hours=t1.hour, minutes=t1.minute, seconds=t1.second)
h2 = timedelta(hours=t2.hour, minutes=t2.minute, seconds=t2.second)

print(str(abs(h2 - h1)).zfill(8))
