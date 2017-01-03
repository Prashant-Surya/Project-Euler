import datetime

start_year = 1901
start_date = 1

count = 0

d = datetime.datetime(start_year, 1, start_date)

while d.year<=2000:
    #print d.year
    if d.day == 1:
        count += 1
    d = d + datetime.timedelta(days=7)

print count
