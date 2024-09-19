str1="Tamil selvan python developer"

str2="Tamil selvan java developer"

str1=str1.lower().split()

str2=str2.lower().split()

inter=set(str1)&set(str2)

print(inter)