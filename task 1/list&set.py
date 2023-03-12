#crete a list with duplicate values and make it unique

l1=[1,2,3,"my"]
l2=[4,"is",5,"karan"]
l1.append(3)
l1.append("name")
l1.append("karan")
print(l1)
l1.extend(l2)
print(l1)
print(set(l1))