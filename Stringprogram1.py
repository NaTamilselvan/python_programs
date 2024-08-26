
str='123 \'tamil\' '

output=''
number=''

for i in str:
    if i.isalpha():
        print(chr(i))
    else:
        number=number+i
else:
    print(output) 
    print(number)       