"""
sum of all the primes below two million.
"""
MAX = 2000000+2
primes = [True]*MAX

for i in range(2, MAX):
    if primes[i]:
        p = 2*i
        while(p<MAX):
            primes[p] = False
            p += i

total = 0
for i in range(2, MAX-2):
    if primes[i]:
        total += i

print total
