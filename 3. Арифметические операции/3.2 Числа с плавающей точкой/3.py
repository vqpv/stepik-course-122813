amount = int(float(input()) * 100 + float(input()) * 100)

vacation = int(amount * 0.1)
food = int(amount * 0.3)
payments = int(amount * 0.05)
leisure = int(amount * 0.15)
savings = int(amount - vacation - food - payments - leisure)

print(f"Отпуск: {vacation // 100} руб. {vacation % 100} коп.")
print(f"Пропитание и еда: {food // 100} руб. {food % 100} коп.")
print(f"Коммунальные платежи: {payments // 100} руб. {payments % 100} коп.")
print(f"Досуг: {leisure // 100} руб. {leisure % 100} коп.")
print(f"Накопления: {savings // 100} руб. {savings % 100} коп.")
