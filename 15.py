
origin = (0,0)

count = 0

def next_move(x,y):
    max_l = 20
    max_r = 20
    global count
    if x==max_l and y==max_r:
        count += 1
        print count
        return
    elif x<=max_l and y<=max_r:
        next_move(x+1,y)
        next_move(x,y+1)
    else:
        return

# Brute force
# next_move(0,0)

from math import factorial

n = 20

fc2 = factorial(2*n)

fc = factorial(n)

count = fc2/(fc*fc)

print count
