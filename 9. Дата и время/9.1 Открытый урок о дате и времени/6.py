import datetime


d1 = datetime.datetime.fromisoformat(input())
d2 = datetime.datetime.fromisoformat(input())

print(abs(int((d2 - d1).total_seconds())))
