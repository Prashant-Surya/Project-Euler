
N = 1001

total=0
prev = 1


for level in range(1, N+1):
    temp = (prev+ 2*(level-1))
    prev = temp
    total += temp
    if level == 1:
        continue
    if level%2 == 0:
        #print prev+level-1
        total += (prev+level-1)
    else:
        #print prev+level
        total += (prev+level)

print total
