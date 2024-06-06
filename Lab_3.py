mylist=["apple", "banana", "cherry"]
for fruits in mylist :
    print(fruits)

mylist.append("Mangoes")
print(mylist)

 countlist = mylist.count("Mangoes")
print(countlist)

idexing_list =  mylist[0] = "Apples is removed "
print(idexing_list)

mylist.remove("Apples is removed ")
print(mylist)

mylist[2] = "Apple"
print(mylist)

mylist.insert(1,("MEAT"))
print(mylist)
mylist.sort()
print(mylist)
mylist.pop(0)
print(mylist)