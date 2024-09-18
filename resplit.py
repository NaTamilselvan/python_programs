import re

print(__name__)

def add():
    
    print("HI i am adding")

def sub():
    
    print("HI i am sub")

s="28:03:1998"


l=re.split(r"[-:]", s)

date,month,year=l

print(date,month,year)