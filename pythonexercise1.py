#January 25, 2026
#Hi, I'm Kai and I'm learning to code.
#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
#tells them the year that they will turn 100 years old.

##Variables for the user name and age. Input fuction is added.

#int as input to be 100% the answer is a number and not text.
my_name = input("What is your name: ")
my_age = int(input("How old are you?: "))

##Age calculator formula.

years_to_hundred = 100 - my_age
current_year = int(input("Enter the current year: "))
future_year = current_year + years_to_hundred

##Edit custom message here.

#%s and %d is a basic argument specifier to callback previous variables in string without too many additions.
#str function is added to convert integers to text.
#added spaces to make it cleaner and not stuck together.
msg = ("Hello %s, you are %d years old in the year " % (my_name, my_age)) + str(current_year) + "." + " In " + str(years_to_hundred) + " years, you will finally turn to the age of 100 by " + str(future_year) + ". "

print(msg)

#New variable for input to make a copy of the message.
num_of_copies = int(input("Enter the number of copies you would like: " ))

### Code to make it print in rows print

print(msg * num_of_copies)
print("Or is this better?")

#New line character is "\n".

msg += "\n"
print(msg * num_of_copies)

