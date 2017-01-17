import math

MAX = 28123

abds = {}

for i in xrange(12, MAX):
    sq = int(math.sqrt(i)) + 1
    factors = []
    for j in xrange(2, sq):
        if i%j == 0:
            factors.append(j)
            if(i//j not in factors):
                factors.append(i//j)
    temp = sum(factors)
    if temp>i:
        abds[i] = True



count = 0

for i in xrange(1, MAX):
    k = i//2 + 1
    flag = False
    for j in abds:
        if j>i:
            break
        else:
            if (j in abds) and (i-j in abds):
                flag = True
                break

    if not flag:
        count += i

print count
