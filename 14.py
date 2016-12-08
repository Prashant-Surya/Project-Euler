'''
Which starting number, under one million, produces the longest chain?
'''


MAX = 1000000

def get_next_num(n):
    if n%2 == 0:
        n = n/2
    else:
        n = 3*n + 1
    return n


max_len = 0
max_num = 0

for num in range(2, MAX):
    count = 0
    i = num
    print num
    while i!=1:
        i = get_next_num(i)
        count += 1
    if count > max_len:
        max_len = count
        max_num = num

print "answer", max_num, max_len

