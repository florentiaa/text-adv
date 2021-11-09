tupleList = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
newList = []

for i in tupleList:
    if i:
       newList.append(i)

print(newList)
