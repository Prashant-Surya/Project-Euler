divisors = [0]*10001

for i in range(1, 10000):
    s = 0
    for j in range(1,i):
        if i%j == 0:
            s += j
    divisors[i] = s

amicables = []
for i in range(1, 10001):
    d = divisors[i]
    if 0<=d<=10000 and i!=d and i == divisors[d]:
        amicables.append(i)

#import ipdb; ipdb.set_trace()
print sum(amicables)
