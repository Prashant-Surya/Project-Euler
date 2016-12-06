"""
Largest prime factor
"""
from math import sqrt
n = 600851475143
max_factor = int(sqrt(n))+1
factors = []
for i in range(2, max_factor):
    if n%i == 0:
        factors.append(i)
factors = factors[::-1]

for i in factors:
    max_limit = int(sqrt(i))+1
    flag = True
    for x in range(2,max_limit):
        if i%x == 0:
            flag = False
            break
    if flag:
        print i
        break
