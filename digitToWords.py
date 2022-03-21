num=input('Enter Number > ')
phonebook={
    '1':'One',
    '2':'Two',
    '3':'Three',
    '4':'Four'

}
for i in num:
    print( phonebook.get(i,'!!!!'))

print(phonebook['1'])
print(phonebook['2'])