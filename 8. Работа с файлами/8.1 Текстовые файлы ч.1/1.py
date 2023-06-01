from collections import Counter

with open("file.txt", encoding="utf-8") as file:
    a = Counter(file.read().replace(',', ' ').replace('.', ' ').split()).most_common()[0]
    word = a[0]
    word_count = a[1]
