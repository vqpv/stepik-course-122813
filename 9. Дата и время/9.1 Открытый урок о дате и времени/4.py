from datetime import date


d1 = date(year=int(input()), month=1, day=1)
d2 = date(year=int(input()), month=1, day=1)

print(abs(d2 - d1).days)
