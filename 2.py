"""
Sum of even valued fibonacci numbers
"""
MAX = 4000000
fibs = [0,1,1]
count = 0
while True:
    x = fibs[-1]+fibs[-2]
    fibs.append(x)
    if x>MAX:
        break
    if x%2 == 0:
        count += x

print count
