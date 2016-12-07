"""
the value of the first triangle number to have over five hundred divisors
"""
from math import sqrt
min_div = 500

num = 10000
start = num*(num+1)/2


while True:
    count = 0
    k = int(sqrt(start)) + 1
    for i in range(2, k):
        if start%i == 0:
            count += 2
    print num, start, count
    if count+2 >= min_div:
        print "answer", num, start
        break
    num += 1
    start += num

