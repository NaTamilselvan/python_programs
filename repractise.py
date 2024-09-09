import re


s="python Hi i week am  tamilselvan pppython developer  weak  ppython  python"

regex=r"we[ae]k"


#match method only find a string in the beginning 
m=re.match(regex,s)

m2=re.search(regex,s)

m3=re.findall(regex,s)

print(m3)


#print(m)
