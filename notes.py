#Print Hello Python 
print("Hello Python!")

#Determine boolean values
print(9<5)
print(9<12)

#Print a list
print(["dtanka","mabadi","aestrada"])

#Use a variable to store a device ID
device_id = "h32rb17"
print(device_id)

print("m50pi31")

#use the type function 
device_id = "h32rb17"

data_type = type (device_id)
print(data_type)

#Demonstrate a type error
#device_id = "h32rb17"
#number = 3
#print(device_id + number)

#Reassign a variable

device_id = "h32rb17"
print(device_id)

device_id = "n73ab07"
print(device_id)

#if starts a conditional statement

#create a conditional
operating_system = "OS 2"
if operating_system == "OS 2" :
    print("Update Needed")


# Add an esle statement
print("Testing Else")
operating_system = "OS 3"
if operating_system == "OS 2":
    print("Update Needed")
else:
    print("No update Needed")

#Iterative Statement - Run forloop with range
for i in range (10):
    print ("Cannot connect to the destination.")

#Iterative Statement - Run while loop 
time = 0
while time <= 10:
    print(time)
    time = time + 2

max_device = 5
i = 1
while i < max_device:
    print("User can still connect to additional devices")
    i = i+1
print ("User has reached maximum number of connected devices")


# Define a function 
def greet_employee():
    print("Welcome! You're logged in.")

# Call a function
greet_employee()

#Greet employees by name
def greet_employee_name(name):
    print("Welcome! You'r logged in",name)


#calling greet employee with name passed as argument
greet_employee_name("Charley Patel")

#Calling function with multiple parameter
def greet_employee_dual_name(first_name, last_name):
    print(f"Welcome! You're logged in {first_name} {last_name}")

greet_employee_dual_name("John","Abraham")

#Sending information outside the function 
#Return information from a function
def calculate_fails(total_attempts,failed_attempts):
    fail_percentage = failed_attempts / total_attempts
    return fail_percentage

calculate_fails(4,2) #this mighnot display
#To display the output of the fail
percentage = calculate_fails(4,2)

print(percentage)

#use information returned from a function
def calculate_login_fails(total_attempts,failed_attempts):
    fail_percentage = failed_attempts/total_attempts
    return fail_percentage

percentage = calculate_login_fails (9,3)

if (percentage >= .5):
    print("Account Locked")
else:
    print("Account is not locked as percentage is",percentage)

#Explore input and output of print
print("This is a string,but",75,"is number.")

#Explore input and output of type
print(type("security"))
print(type(73.2))

#Explore max
a =3
b =9
c =6
print(max(a,b,c))

#Explore Sorted function - It is very important
#Use the sorted function
username = ["elasrson","bmoreno","tshah","sgilmore","erab","gesparza","alevitsk","wjaffrey"]
print(sorted(username))

#standard library modules 
#re
#csv
#glob
#os
#time
#datetime

my_string="Security"

#converting an integer into a string
new_string = str(123)
print(type(new_string))

#len() - Returns the number of elements in an object
#print the length of a string "Hello"
print(len("Hello"))

#String concatnation - The process of joining two strings together
# Concatenate two strings
print("Hello"+"Worlds!")

#Method - A function that belongs to a specific data type
#Method appear after the string. Two common method are upper() and lower()
#Apply upper method to "Hello"
print("Hello".upper())
#Apply lower method to "Hello"
print("Hello".lower())  

#Searching in logs
#Index - A number assigned to every element in a sequence that indicates its position
print("Hello"[1:4])

#We can extract large part of string using specifying a set of indices
#slice 
#Extract a slice from a string
print("Hello"[1:4])

#Search in string 
#.index() method - Finds the first occurrence of the input in a sting and returns its location
# Use the index string method
print("Hello".index("e"))

#Search for charecter "L"
print("HELLO".index("L"))

#Strings are immutable - It can not be changed after it is created and assigned a value
#my_string = "HELLO"
#my_string[1] ="A"
#this will give error


#List can be changed and are immutable
my_list = ["a","b","c","d","e"]

print(len(my_list))

print(my_list[1])

#List Concatination is combing two list into one by placing the elements of secondlist directly after the elements of first list
#Concatenate two list
my_list = ["a","b","c","d","e"]
number_list = [1,2,3,4]
print(my_list+ number_list) #concatnation of list

#Change a specific element in a list
my_list = ["a","b","c","d","e"]
my_list[1] = 7
print(my_list)

#method for modifying list
#.insert() Add an element in a specific position in a list
my_list.insert(1,8)
print(my_list)

#.remove() Removes the first occurrence of a specific element in a list
# Use the remove method
my_list = ["a","b","c","d","e"]
my_list.remove("d")
print(my_list)

#Algorith - A Set of rules that solve a problem
IP = ["192.567.xx.xx","192.501.xx.xx","180.664.xx.xx","192.668.xx.xx","184.690.xx.xx"]

address = "198.567.xx.xx"
#Extract the first three characters of an IP address
temp_var = address[0:3]
print(temp_var)
first_octet =[]
#.append() - Adds input to the end of a list

for i in IP:
    temp_address = i
    temp_var = temp_address[0:3]
    #first_octet = first_octet.append(temp_var) - This wont work
    first_octet.append(temp_var) # This works

print (first_octet)


#Regular Expression - A Sequence of charecters that forms a pattern

'''
+ Represents one or more occurrences of a specific character
a+ any length in which a is repeated
\w Matches with any alphanumeric character but it doesnt match symbols
"1","k",i"  are places where \w will match
\w+@\w+\.\w+ == will match all email address 
'''
test_string = "Device IDs: a37rz87 io2aap4 32rb5a2 9aaa95y"

#Extract email address
import re
email_log = """Email recieved June 2 from user1@email.com. 
            Email recieved June 2 from user2@gmail.com
            Email rejected June 2 from invalid_email@email.com""" #multi line string so three quotation mark


#re.findall() = Returns a list of mathces to a regular expression 
print(re.findall(r"\w+@\w+\.\w+",email_log))

#extract IP address
paragraph = "The servers at 10.0.0.1 and 10.0.0.254 forward traffic to 172.16.0.1, while client devices like 192.168.0.10, 192.168.0.11, and 192.168.1.5 connect through gateways 192.168.0.1 and 192.168.1.1; external services run on 8.8.8.8, 1.1.1.1, 203.0.113.5, and 198.51.100.42, and backup nodes 10.1.1.1, 10.1.1.2, and 10.2.2.2 synchronize logs with monitoring hosts at 192.0.2.1 and 192.0.2.2."

print(re.findall(r"(?:(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)",paragraph))
