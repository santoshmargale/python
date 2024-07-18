#5.  list:mutable(because it is heterogenous and indixing is allowed and change the index value )
l=[12,"pranav","@",18.2]
print(l)
# Indexing of list means access 1 element and and any element of list by following method
print(l[0])
print(l[2])
print(l[-1])
print(l[::-1])
# check of length of list we use len() function
print(len(l))
# checking the for loop
for i in range(len(l)):
  print(i)
# print list in desired way
for i in range(len(l)):
  print(f"the element number{i+1} of given list is:{l[i]}")
# To check the mutable
l[0]="Zcoer"
print(l)
