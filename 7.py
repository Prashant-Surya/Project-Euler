"""
10001st prime
"""
from math import sqrt

primes = [2,3]

start = 4

while len(primes)<10001:
    k = int(sqrt(start)) +1
    flag = True
    for i in range(2, k):
        if start%i==0:
            flag=False
            break
    if flag:
        primes.append(start)
    start += 1


print primes[-1]
