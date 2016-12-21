'''
 all the numbers from 1 to 1000 (one thousand) inclusive were written out in
 words, how many letters would be used?
'''

import inflect # third party :P

inf = inflect.engine()

def get_count(word):
    count = 0
    for i in word:
        if i != ' ' and i!='-':
            count += 1
    return count


total = 0

for num in range(1,1001):
    total += get_count(inf.number_to_words(num))

print total
