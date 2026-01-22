#These notes are follow along the video example
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
