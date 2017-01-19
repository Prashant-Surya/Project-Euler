primes = [False]*1001

for i in range(2, 998):
    M = 1000
    if not primes[i]:
        limit = M/i
        for j in range(1, limit+1):
            if i*j>1000:
                break
            primes[i*j] = True

p = {}
for i in range(2, len(primes)):
    if primes[i]:
        p[i] = 1

new_primes = {}

MAX_VAL = 0
MAX_PROD = 0

def get_val(n,a,b):
    '''n^2+(a*n)+b should be prime'''
    global primes
    val = n**2 + a*n + b
    if val<=0:
        return False
    if val<1000:
        return primes[val]
    elif val in new_primes:
        return new_primes[val]

    from math import sqrt
    top = int(sqrt(val))+1
    flag = True
    for i in range(2, top):
        if val%i==0:
            flag = False
            break
    new_primes[val] = flag
    return flag

#import ipdb; ipdb.set_trace()
for a in range(1, 1000, 2):
    for b in p:
        if b>1000:
            break
        n = 0
        while get_val(n,a,b):
            n += 1
        if n > MAX_VAL:
            MAX_VAL = n
            MAX_PROD = a*b

        n = 0
        while get_val(n,-a,b):
            n += 1
        if n > MAX_VAL:
            MAX_VAL = n
            MAX_PROD = -a*b

        n = 0
        while get_val(n,a,-b):
            n += 1
        if n > MAX_VAL:
            MAX_VAL = n
            MAX_PROD = -a*b

        n = 0
        while get_val(n,-a,-b):
            n += 1
        if n > MAX_VAL:
            MAX_VAL = n
            MAX_PROD = a*b


print MAX_PROD
