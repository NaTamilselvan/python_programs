lst=[1,2,3,4,5,6,7,8,9]

print(len(lst))

#lst[::2]=["assign"]

lst[::2]=[0,0,0,0,0]

print(lst)

lst+=[1,2,4]

lst.extend([5,4,3])

#lst.remove(34)

print(lst)

lst[1:4]=[99,23,"8",10,10,10]

print(lst)


del lst[3]

print(lst)

del lst[::2]

print(lst)