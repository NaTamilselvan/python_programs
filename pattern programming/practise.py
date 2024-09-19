from collections import Counter
import re
def findacharcters(s):
    
    regex="ae"
    
    
    l=re.findall(regex, s)
    
    print(l)
    
    
''' This program for find matching character '''  
    
s=input("Enter the String\n")    
st=set({})
s2='aeiou'
for i in s:
    print(i)
    if i in s2:
        print(i,"The 2 nd")
        st.add(i)
#result=Counter(s)

#print(result)


print(st)



#findacharcters(s)
    
    