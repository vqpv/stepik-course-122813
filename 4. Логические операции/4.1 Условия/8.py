s_1, s_2, s_3 = input(), input(), input()

l_1 = len(s_1)
l_2 = len(s_2)
l_3 = len(s_3)
m = s_1

if l_2 <= l_1:
    m = s_2
if l_3 <= len(m):
    m = s_3
    
print(m)
