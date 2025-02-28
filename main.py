import datetime
format = '%d/%m/%Y'

dates = []
with open("namedate.txt") as f:
    for line in f:
        line = line.strip()
        name, date = line.split(',')
        date = datetime.datetime.strptime(date.strip(), format)
        dates.append((name, date))

dates.sort(key=lambda s: s[1])

for name, date in dates:
    print(name, date.strftime(format))
