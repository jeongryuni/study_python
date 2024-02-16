total = 0

with open('data/chicken.txt', 'r') as f:
    for Line in f:
        Line = Line.strip()
        Line_split = Line.split('일:')
        All_day = Line_split[0]
        All_price = Line_split[1]

        total = total + int(All_price)
print(total)
print(All_day)

print(total/int(All_day))