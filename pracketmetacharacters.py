import re 


s="""
gogle

google
gooogle
 gooogle
goooogle
goooooogle
gooooooogle


"""


regex=r"go{2,}gle"


l=re.findall(regex, s)


print(l)

print(len(l))
