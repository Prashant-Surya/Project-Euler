#f = open('18.prob', 'r')
f = open('p067.txt', 'r')
data = []
for line in f:
    row = line.rstrip('\n').split(' ')
    row = map(int, row)
    data.append(row)

f.close()
#print data
#data = [[3], [7,4], [2,4,6], [8,5,9,3]]
nums = []
i = 0

out = []

#import ipdb; ipdb.set_trace()
for row in range(0, len(data)):
    current = data[row]
    max_len = len(out)
    if not out:
        out = [current[0]]
    else:
        temp = []
        for index in range(0, len(current)):
            cur_ele = current[index]
            #print row, index, cur_ele
            if index == 0:
                #import ipdb; ipdb.set_trace()
                temp.append(out[0]+cur_ele)
            elif index == len(current)-1:
                temp.append(out[-1]+cur_ele)
            else:
                #import ipdb; ipdb.set_trace()
                temp.append(max(current[index]+out[index], current[index]+out[index-1]))
        out = temp

print max(out)
