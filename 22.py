f = open('p022_names.txt', 'r')

data = f.readlines()[0]

f.close()

data = data.split(',')

data = [i.replace('"','') for i in data]

data.sort()

def get_alpha_score(s):
    score = 0
    for i in s:
        score += 1 + ord(i) - ord('A')
    return score

total = 0

for i in xrange(0, len(data)):
    pos = i+1
    score = get_alpha_score(data[i])
    total += pos*score

print total
