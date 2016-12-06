"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

MAX = 1000

def check(a,b):
    TP = 5*(10**5)
    lhs = 1000*(a+b)
    rhs = a*b + TP
    if lhs == rhs:
        print a,b, 1000-a-b
        print a*b*(1000-a-b)
        return True
    else:
        return False

for a in range(1, MAX):
    flag = True
    for b in range(a+1, MAX):
        if check(a,b):
            flag = False
            break
    if not flag:
        break
