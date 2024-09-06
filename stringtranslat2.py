s="good morning01"


e="mor"

ch="eve"


table=s.maketrans("mor","eve","01")

s2=s.translate(table)


print(s)
print(s2)