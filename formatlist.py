l=[10,20,30]

s="{0[1]} {0[1]} {0[2]}".format(l)

print(s)

s2="{} {} {} ".format(*l)

print(s2)