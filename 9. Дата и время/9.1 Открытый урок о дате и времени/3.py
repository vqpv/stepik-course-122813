import calendar
from datetime import date


d1 = date.fromisoformat(input())
d2 = date.fromisoformat(input())

if d1.year == d2.year and d1.month == d2.month:
    print((d2 - d1).days + 1)
else:
    print(calendar.monthrange(d1.year, d1.month)[1] - d1.day + 1)
