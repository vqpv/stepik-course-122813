with open('ex.txt', 'r', encoding='utf-16') as f:
    answer = f.read()
with open('ex.txt', 'a', encoding='utf-16') as f: 
    f.write("\nhacked")
