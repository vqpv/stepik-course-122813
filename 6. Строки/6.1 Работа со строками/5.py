from string import ascii_lowercase

s = input()
step = int(input())

for i in s:
    print(ascii_lowercase[(ascii_lowercase.find(i) + step) % 26], end="")
