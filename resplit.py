import re

<<<<<<< HEAD
print(__name__)

def add():
    
    print("HI i am adding")

def sub():
    
    print("HI i am sub")

=======
>>>>>>> 2347047ace021745da41456624bbbb620e44aeaa
s="28:03:1998"


l=re.split(r"[-:]", s)

date,month,year=l

print(date,month,year)