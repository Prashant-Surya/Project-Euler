
def string_sum(a, b):
    '''
    considering a<=b
    :params a,b are strings
    '''
    diff = len(b)-len(a)
    a = '0'*diff + a
    out = ""
    carry = 0
    for i in xrange(len(b)-1, -1, -1): #decrement loop
        temp = int(b[i])+int(a[i])+carry
        temp = str(temp)
        if len(temp)>1:
            carry = int(temp[0])
            temp = temp[1:]
        else:
            carry = 0
        out = temp[0] + out

    if carry>0:
        out = str(carry) + out

    return out

numbers = ['1', '1']

#print string_sum('99', '992')
count = 2

while True:
    out = string_sum(numbers[-2], numbers[-1])
    if len(out) == 1000:
        print count+1
        break
    count += 1
    numbers.append(out)
