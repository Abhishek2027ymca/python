

thisset = {"monday", "tuesday", "wednesday"}  # creating
print(thisset)


for x in thisset:          #accessing
  print(x)


thisset.add(" Sunday")            #adding
         
print(thisset)


thisset.discard("wednesday")

print(thisset)

sett = {"abhishek", "himanshu", "aryan" , "monday"}


set3 = thisset.union(sett)
print(set3)

set3 = thisset.intersection(sett)
print(set3)



set3 = thisset.difference(sett)

print(set3)


