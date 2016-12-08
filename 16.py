'''
sum of the digits of the number 2^1000
'''

n = 1000

p = str(2**1000)

l = list(p)

s = 0
for i in l:
    s += int(i)

print s
