from datetime import date


day_1 = date.fromisoformat(input())
day_2 = date.fromisoformat(input())

try:
    d1 = day_1.replace(year=day_2.year)
    d2 = day_2.replace(year=day_1.year)
    print(d1, d2, sep="\n")
except ValueError:
    print("Год изменить невозможно")
