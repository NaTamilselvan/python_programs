import re

test="hi i am tamil selvan hi i am python devloper  amil  ttttamil"

regex="am "

#match method ku only beginning of word
#search method search entire string but first occurence its end 
#find all tkaes ablity entire stiring use meta cahracters . all 
#\. escap string only .
#pipe either
#* indicalte matching first character not present it takes and 
#atteched begin the character any ltter also take it 
#?not present 0 not take 
#+character 


regex1="t+amil"

l=re.findall(regex,test)

print(l)