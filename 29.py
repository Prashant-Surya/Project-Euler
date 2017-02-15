N = 100

nums = set()


for i in xrange(2, 101):
    for j in xrange(2, 101):
        k = i ** j
        nums.add(k)

print len(nums)
