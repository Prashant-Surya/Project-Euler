"""
Largest palindrome product of 3 digit numbers
"""
palinds = []
for i in range(100, 1000):
    flag = True
    for j in range(100, 1000):
        p = str(i*j)
        if p == p[::-1]:
            palinds.append(int(p))
print max(palinds)
