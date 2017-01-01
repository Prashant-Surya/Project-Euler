data = {}

def SOS(num):
    num = str(num)
    total = 0
    for i in num:
        total += (int(i)**2)
    return int(total)

M = 10000000

for i in range(1, M+1):
    s = i
    while True:
        s = SOS(s)
        if s == 1 or s==89:
            data[i] = s
            break
        elif s in data:
            data[i] = data[s]
            break

count = 0
for i in data:
    if data[i] == 89:
        count += 1
print count
