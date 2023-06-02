try:
    with open("data.txt", "r", encoding="utf-8") as data:
        text = data.read()
        with open("out.txt", "w", encoding="utf-8") as out:
            out.write(text)
except FileNotFoundError:
    with open("data.txt", "w", encoding="utf-8") as data:
        data.write("Третий фактор")
