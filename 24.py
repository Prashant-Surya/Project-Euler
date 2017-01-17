from math import factorial

numbers = {}

for i in range(0,10):
    numbers[i] = 1

def main():
    global numbers
    MAX = 1000000
    count = MAX
    out = ""
    for i in xrange(9, -1, -1):
        print "init", out
        #import ipdb; ipdb.set_trace()
        f = factorial(i)
        num = count / f
        count = count%f   #$ - (num*f)
        keys = numbers.keys()
        print i, keys, num, keys[num]
        key = keys[num]
        out += str(key)
        numbers.pop(key)
    print out

if __name__ == '__main__':
    main()
