#January 26, 2026

#Python Exercise 2

##Ask for user input 
number = int(input("Enter a number: "))

##Checks number is even or odd and prints
if number % 4 == 0:
    print("Number is multiple of 4")
elif number % 2 == 0:
    print("Number is an even number")
else:
    print("Number is an odd number")

##New input to ask one number to check, and one number to divide
#Added variables for quick shortcuts to callback
msg = "Enter a number to"
a = "check"
b = "divide"
num_1 = int(input("%s %s: " % (msg, a)))
num_2 = int(input("%s %s: " % (msg, b)))

#Checks number is even or odd and prints
if num_1 % num_2 == 0:
    print("Number is an even number")
else:
    print("Number is an odd number")
