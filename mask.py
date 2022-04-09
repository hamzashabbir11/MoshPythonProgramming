card_no =input('Enter 12 Digit Card No ')
l=[]
masked=''
for i in range(len(card_no)):
    l.append(card_no[i])

for j in range(0,12):

    l[j]='*'

masked=masked.join(l)
print(masked)