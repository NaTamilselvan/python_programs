import re



s="HI i am python developer"

regex="developer"

math=re.search(regex, s)

start,end=math.span()


print(start,end)

print(s[start:end])

print(s[math.start():math.end()])

print(math.pos)
