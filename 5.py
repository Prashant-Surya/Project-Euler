"""
Smallest positive integer divisible by all in (1, 20)
"""
from math import sqrt

primes = {}
for i in range(2,21):
    k = int(sqrt(i)) + 1
    flag = True
    for j in range(2,  k):
        if i%j == 0:
            flag = False
            break
    if flag:
        primes[i] = 1

for i in range(4,20):
    for p in primes:
        c = 0
        num = i
        while num%p == 0:
            c += 1
            num = num/p
        primes[p] = max(primes[p], c)

print primes
prod = 1

for p in primes:
    prod *= pow(p, primes[p])

print prod
