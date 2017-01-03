carry = 0

outs = [1,0,0]

mult = 99

def csum(a,b):
    '''a,b are strings'''
    carry = 0
    a = a[::-1]
    b = b[::-1]
    l = max(len(a), len(b))
    out = ""
    for i in range(0,l):
        temp = 0
        if i<len(a):
            temp += int(a[i])
        if i<len(b):
            temp += int(b[i])

        temp += carry
        out = str(temp%10) + out
        temp /= 10
        carry = temp
    if carry > 0:
        out = str(carry)+out
    return out

'''
for i in range(99,0,-1):
    num = i #list(str(i))[::-1]
    temp = []
    while num>0:
        d = num%10
        num = num/10
        for k in outs[::-1]:
            res = k*d + carry
            if len(str(res))>1:
                carry = str(res)[1]
            else:
                carry = 0
            temp.append(res%d)
'''

from math import factorial

s = factorial(100)
l = list(str(s))

s = map(int, l)

print sum(s)
