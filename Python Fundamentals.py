# Pyhton Fundamentals
# Variable
# Variable in Python is used to store data .
# Reassign and Compute
name = "Jerry"
print(name)
name = "Tom"
print(name)



a = 10
b = 20
c = a+b
print(c)



# What is a Datatype?
#Datatype is a classification of data which tells the compiler or interpreter how the programmer intends to use the data. Python has various standard data types that are used to define the operations possible on them and the storage method for each of them.

a = 10    # int
b = 'Manish'  #str
c = 10.5  #float
d = True  #bool
h = None #NoneType

#Dynamic - Pyhton re-detects
a = "Kritika"
#Built-In Functions
print(type(a))



#Primitive Vs Collection Data Types
#Primitives are the most basic data types available within the programming language. They serve as the building blocks for data manipulation and storage. In Python, primitive data types include integers, floats, strings, and booleans.
#Collection data types, on the other hand, are more complex structures that can hold multiple values or elements. They allow for the organization and manipulation of groups of data. In Python, common collection data types include lists, tuples, sets, and dictionaries.

#Primitive - One value
a = 10
print(a)

#Collection - Multiple values
arr = [10,20,30,40,50]            #list of integers
Groceries = ["Milk","Eggs","Bread","Butter"]    # list of strings
pair = (10,20)              #tuple of integers
dict = {"Name": "Kritika", "Age":20, "Class":"Btech"}   #dictionary 
term = {10,20,"Kritika, 10.5"}         #set
print(pair)
print(arr)
print(Groceries)


#Working with Quotes
#Escape - use\before the inner quote
#Mix types - outer single, inner double
#Triple quotes - For strings spanning multiple lines
#Tip- triple quotes preserve line breaks

#1Escape
print("Hi \"Python\"")
#2. Mix quote types
print('Hi,"Python"')
#3. Triple quotes
print("""Hi
Python""")


#Built-in Functions
#print()displays information to the user
#input()receives information from the user, it always returns a string 
name = input("Enter your name: ")
print(name)


#The print() Function
#Why Use print()
#Communicate- Show output to the user
#Display - results of calculations
#Debug - find where the code breaks
#Test - verify the output is correct

#Basic syntax
print("Kritika loves tea.") 
#Multiple 
print("Sum  = ", 10+5)

#Variables & Layout
total_qty = 35
price = 100
revenue = price*total_qty
print(revenue)

print("""Learning path:
      -Python Basics
      -Data Engineering
      -AI Engineering""")


#Read Text
name = input("Enter your name: ")
print("Hello,", name)

#Read a number
age = int(input("Enter your age: "))
print("Next year." , age+1)



#Functions and Methods
#Standalone vs Class-Bound 
#Function-standalone:print(x),type(x), len(x)
#Method- class-bound: "text".upper()

text ="Kritika"
num=90

#Functions-work on either
print(type(text))
print(len(text))

#Methods - class specific
print(text.upper())
print(len(text))

#num.upper() ->Attribute Error
#int object has no attribute


=================================STRING DATATYPE=====================================
#STRING DATATYPES

#Cleaner Code with variables
#DRY & f-strings


#without variables
print("My name is Kritika")
print("I love Python")

#with variables
name = input("Enter your name: ")
language = input("Enter language you love: ")
print(f"My name is {name}.")
print(f"{name} loves {language}.")


#Escape Sequences
print("Line1\nLine2")
print("Hii\tEveryone")
print("Path: C:\\Users\kritika kumari\OneDrive\Desktopp")
print("She said\"Hi\"")

#Strings - Transforamtions
date = "2024/06/10"
print(date.replace("/","-"))   #replace()-substitute substring
first = "Kritika" ;last = "Kumari"
print(f"{first}{last}")

csv = "Kritika,20,Ny"
print(csv.split(",")) #split()- break into a list

print("="*20)


#Strings - Slicing & Indexing
code = "Kritika-20"
print(code[0])
print(code[-1])
print(code[0:6])
print(code[-2:])

date ="2026-05-09"
print(date[0:4],date[5:7], date[-2:])

print(code[0:9:2])   #stride

