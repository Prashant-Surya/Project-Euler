def recurrence(num):
    f = float(1)
    start = 10
    outs = {}
    count = 0
    while True:
        count += 1
        while start<num:
            start *= 10
        start = start%num
        if start ==0:
            break
        if start in outs:
            return count-outs[start]
        else:
            outs[start] = count

    return 0

if __name__ == '__main__':
    MAX = 0
    MAX_I = 0
    for i in range(2, 1000):
        r = recurrence(i)
        print i,r
        if r>MAX:
            MAX = r
            MAX_I = i
    print "Max number and cycle length"
    print MAX_I, MAX
