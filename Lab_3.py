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

print(mylist[1:3])
print(mylist[:])
print(mylist[:-1])

# eg:Dicitionay and practice
my_dicitionary = {
"Name": "Sibtain",
"Sex": "Male",
"Age": 19,
"Year" : 2024
}

print(my_dicitionary)

my_dicitionary.pop("Name")
print(my_dicitionary)
my_dicitionary["Year"] = "Since"
print(my_dicitionary)
my_dicitionary.get("Age")
print(my_dicitionary)

# loops
i =1
while i < 6:
    i = i +1
    print(i)
