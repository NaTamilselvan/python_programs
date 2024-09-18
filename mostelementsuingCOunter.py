from collections import Counter

l=[1,3,3,4,4,5,1,4]


k=Counter(l)

print(k)


s=list(k.elements())

q=list(k.most_common(2))


print(q[1][0])


#print(s)



#print(q)
         
