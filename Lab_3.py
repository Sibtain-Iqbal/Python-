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

Value = 1
while Value < 20:
    if Value !=0:
        Value += 1
        print(Value)

# For Loop
numbers = [1,2,3,4,5,6,7,8]
for num in numbers :
    if numbers != num**2 :
        print(num)

languages = ['Swift', 'Python', 'Go', 'JavaScript']
languages.append("Golang")
print(languages)

All_numbers = []
num_a = All_numbers.append( int(input("Enter the Value : ")))
num_b =All_numbers.append( int(input("Enter the value :  ")))
num_c = All_numbers.append(int(input("Enter The Value:  ")))
All_numbers.sort()
minimum_value = All_numbers[0:1]
sums = sum(All_numbers)
min_3 = min(All_numbers)
print(f"The Sum of all value in this list is : { sums}")
print(f"The minimum  value in this list is : { min_3}")
print(All_numbers)
# problems




print("Welcome to the Number Guessing Game! and I have chosen a number between 1 and 10. Try to guess it.")
secrete_number = 9
guess = None
while guess != secrete_number :
    guess = int(input("Enter guessing number : "))
    if guess == secrete_number :
        print(f"Congratulation you have select correct number : {secrete_number} ")
    else :
        print("That is incorrect. Guess again.")
print("Thanks for playing!")