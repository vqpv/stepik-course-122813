s = input()

c = max_c = 1
result = s[0]

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        c += 1
    else:
        c = 1
    if max_c <= c:
        max_c = c
        result = s[i]

print(result, max_c, sep="\n")
