f = open('18.prob', 'r')

data = []
for line in f:
    row = line.rstrip('\n').split(' ')
    row = map(int, row)
    data.append(row)

f.close()
print data
#data = [[3], [7,4], [2,4,6], [8,5,9,3]]
nums = []
i = 0
"""
nums.append([data[0][0]])
root = data[0][0]

ex = [root+data[1][0], root+data[1][1]]
nums.append(ex)
for i in range(0,2):
    new = []
    row = data[2]
    new.append(ex[i]+row[i], ex[i]+row[i+1])
    ex = new
    nums.append(new)
for row in range(1, len(data)):
    cur = data[row]
    M = max(cur[i], cur[i+1])
    i = cur.index(M)
    total += M
    nums.append(M)

for row in range(3, len(data)):
    cur = data[row]
    new = []
    for i in range(0, len(ex)):
        temp_row = []
        temp = ex[i]
        for j in temp:
            temp_row.append(j+cur[j])
            temp_row.append(j+cur[j+1])
        new.append(temp_row)

out = []
import ipdb; ipdb.set_trace()
for row in range(0, len(data)):
    current = data[row]
    new_out = []
    if not out:
        out = [current]
    else:
        for l in range(0, len(out)):
            cur_out = out[l]
            new = []
            for num in cur_out:
                new.append(num+current[l])
                new.append(num+current[l+1])
            new_out.append(new)
        out = new_out
"""
out = []

#import ipdb; ipdb.set_trace()
for row in range(0, len(data)):
    current = data[row]
    max_len = len(out)
    if not out:
        out = [current]
    else:
        temp = []
        for index in range(0, len(current)):
            cur_ele = current[index]
            print row, index, cur_ele
            if index == 0:
                temp.append([out[0][0]+cur_ele])
            elif index == len(current)-1:
                temp.append([out[-1][0]+cur_ele])
            else:
                #temp.append(current[i]+out[i])
                #temp.append(current[i]+out[i-1])
                temp_store = 0
                temp_list = []
                for k in out[index]:
                    temp_store = cur_ele + k
                    temp_list.append(temp_store)
                temp_store = 0
                for k in out[index-1]:
                    temp_store = cur_ele + k
                    temp_list.append(temp_store)
                temp.append(temp_list)
        out = temp
        

#print total
#print nums

M = 0

for i in out:
    if max(i)>M:
        M = max(i)

print M
