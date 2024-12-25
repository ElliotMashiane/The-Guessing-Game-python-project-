# print("Hello World")
# print("*"*10)

# primitive types

# 1. VARIABLES

# STUDENT_COUNT = 1000  # integer
# RATINGS = 4.99  # float
# IS_AVAILABLE = True  # boolean
# COURSE_NAME = "Python Programming"  # String
# print(STUDENT_COUNT)


# 2. VARIABLE NAMES

# GIVE MEANINGFUL NAMES TO YOUR VARIABLES AND BE CONSISTENT AND FORMAT ACCORDINGLY

# 3. STRINGS
# COURSE = "Python Programming"

# we use the len function to count the number of characters in a string
# print(len(COURSE))
# we use the square bracket to get access to a specific character in a string
# print(COURSE[0])
# print(COURSE[0:3])
# print(COURSE[-1])
# print(COURSE[0:6])
# print(COURSE[0:3])

# 4. ESCAPE SEQUENCE
# \"
# \'
# \\
# \n  NEW LINE

# COURSE1 = "PYTHON \nPROGRAMMING"
# print(COURSE1)


# 5. FORMATTED STRINGS
# F"{}" ALLOWS YOU TO PUT ANY VALID EXPRESSIONS IN THE CURLY BRACES

# FIRST = "ELLIOT"
# LAST = "MASHIANE"
# FULL = F"{FIRST} {LAST}"
# print(FULL)

# 6. STRING METHODS

# COURSE2 = "     Python Programming"
# print(COURSE2.upper()) #changes all letters to Upper Case letters
# print(COURSE2.lower()) #changes all letters to Lower case letters
# print(COURSE2.strip()) #closes all the empty spaces around words and letters
# print(COURSE2.replace("n", "c")) #this method replaces the first letter in quotes with the 2nd letter in quotes
# print("t" in COURSE2) #this method returns a boolean value if the statement is true or false
# print("mike" not in COURSE2) #this method returns a boolean value if the statement is true or False

# 7. Numbers

# x = 1  # integer
# x = 1.1  # float
# x = 1+2j  # complex numbers

# math operations

# print(10+3)  # addition
# print(10-3)  # subtraction
# print(10*3)  # multiplication
# print(10/3)  # division
# print(10//3)  # division without remainder
# print(10 % 3)  # division showing only the remainder
# print(10**3)  # exponential


# x = 10
# x = x + 3  argmented assignment operator
# x += 3    another argmented assignment operator

# 8. Working with numbers

# print(round(3.7)) functions to use when working numbers these are built in
# print(abs(-66))

# import math
# it is ideal to work with the math module which is built in python

# print(math.exp(4))
# check documentation through google for more methods


# 9. TYPE CONVERSION
# X = input("x:")
# y = int(X) + 1
# print(y)


# FUNDAMENTAL PROGRAMMING
# CONTROL FLOW
# COMPARISON OPERATORS

# print(45 > 56)
# print(45 <= 56)
# print(45 == 56)
# print(1 < 56)

# 1. CONDITIONAL STATEMENTS (if, elif and else statements)
# TEMPERATURE = 12

# if TEMPERATURE > 30:
#    print("yerr! its Hot")
#    print("Drink Water!!")

# else:
#    print("stay cool!!")

# print("done!")

# 2. Ternary Operator
# AGE = 2

# MESSAGE = "Eligible" if AGE >= 18 else "Not eligible"

# print(MESSAGE)

# 3. LOGICAL OPERATORS (and, Or, not)

# high_income = True
# good_credit = False
# student = True

# if (high_income or good_credit) and not student:
#    print("Eligible")

# else:
#   print("Not Eligible")

# 4. Chaining Comparison Operators (What i call the AND statement as in Mathematics)

# age = int(input("enter your age:"))
# if 18 <= age < 30:
#    print("They are old enough")
# elif 0 <= age < 18:
#    print("Still Young!!")

# else:
#    print("Over Qualified")

# 5. For loops
# for number in range(1, 4):
#    print("Attempt", number, number*".")


# 6. For>>Else statements

# successful = False

# for number in range(3):
# print("Attempt")
# if successful:
# print("Message sent successfully!")
# break

# else:
# print("3 Attempts made Sending of Message was Unsuccessful!!!")

# 7. Nested loops

# for x in range(5):
#     for y in range(3):
#         print(f"({x};{y})")


# Activity on "primitive Types" lesson

# Exercise: Primitive Types Manipulation
# Write a Python program that does the following:

# Prompt the user to enter the following values:

# A string (e.g., their name).
# An integer (e.g., their age).
# A floating-point number (e.g., their height in meters).
# A boolean value (e.g., whether they like pizza, using True or False).

# Perform the following tasks:

# Print the types of all the entered values using the type() function.
# Convert the integer to a floating-point number and print the result.
# Convert the floating-point number to an integer and print the result.
# Convert the boolean to a string and concatenate it with another string (e.g., "Likes pizza: ") and print the result.
# Reverse the entered string and print it.

# my solution
# name = input("Enter Your Name:")
# age = int(input("Enter Your Age:"))
# height = float(input("Enter Your Height:"))
# pizza_question = bool(input("Do You Like Pizza(True or False):"))

# print(name)
# print(age)
# print(height)
# print(pizza_question)

# print(type(name))
# print(type(age))
# print(type(height))
# print(type(pizza_question))


# age_as_float = float(age)
# height_as_interger = int(height)
# bool_as_string = str(pizza_question)
# concatenated_strings = "Likes pizza:" + " " + bool_as_string

# print(f"age as float: {age_as_float}")
# print(f"height as integer: {height_as_interger}")
# print(concatenated_strings)
# print(name[::-1])

# chatgpt solution

# # Input from the user
# name = input("Enter Your Name: ")
# age = int(input("Enter Your Age: "))
# height = float(input("Enter Your Height: "))
# pizza_question = input("Do You Like Pizza (True or False): ").strip()

# # Converting pizza_question to a boolean
# pizza_question = True if pizza_question.lower() == "true" else False

# # Display inputs
# print(name)
# print(age)
# print(height)
# print(pizza_question)

# # Display types
# print(type(name))
# print(type(age))
# print(type(height))
# print(type(pizza_question))

# # Type conversions
# age_as_float = float(age)
# height_as_integer = int(height)
# bool_as_string = str(pizza_question)
# concatenated_strings = "Likes pizza: " + bool_as_string

# # Output results
# print(f"Age as float: {age_as_float}")
# print(f"Height as integer: {height_as_integer}")
# print(concatenated_strings)
# print("Reversed name:", name[::-1])

# primitives types activity 2

# while True:
#     try:
#         bill = float(input("Enter the bill amount:"))
#         if bill < 0:
#             print("Error: Bill amount cannot be negative. Please enter a valid value")
#             continue

#         tip = int(input("Enter the tip percentage:"))
#         if tip < 0:
#             print("Error: Bill amount cannot be negative. Please enter a valid value")
#             continue

#         break
#     except ValueError:
#         print("Error: Please enter numeric values only.")


# bill_amount = f"Bill Amount: $ {bill}"
# tip_calulated_from_bill = bill*(tip/100)
# tip_amount = f"Tip Amount: $ {tip_calulated_from_bill}"
# total_amount = bill + tip_calulated_from_bill
# total_rounded = round(total_amount, 2)
# total_amount_formated = f"Total Amount: $ {total_rounded}"

# print(bill_amount)
# print(tip_amount)
# print(total_amount_formated)


# chat gpt solution
# while True:
#     try:
#         bill = float(input("Enter the bill amount: "))
#         if bill < 0:
#             print("Error: Bill amount cannot be negative. Please enter a valid value.")
#             continue  # Restart the loop if input is invalid

#         tip = int(input("Enter the tip percentage: "))
#         if tip < 0:
#             print("Error: Tip percentage cannot be negative. Please enter a valid value.")
#             continue  # Restart the loop if input is invalid

#         break  # Exit the loop if both inputs are valid
#     except ValueError:
#         print("Error: Please enter numeric values only.")

# # Calculations
# bill_amount = f"Bill Amount: $ {bill:.2f}"
# tip_calculated_from_bill = bill * (tip / 100)
# tip_amount = f"Tip Amount: $ {tip_calculated_from_bill:.2f}"
# total_amount = bill + tip_calculated_from_bill
# total_amount_formatted = f"Total Amount: $ {total_amount:.2f}"

# # Output
# print(bill_amount)
# print(tip_amount)
# print(total_amount_formatted)


# lesson : # iterables (strings,lists, range, lists etc....)

# for x in "python":
#     print(x)

# for x in range(8):
#     print(x)

# Lesson: While Loop


# COMMAND = ""

# while COMMAND.lower() != "quit":
#     COMMAND = input(">>")
#     print("$", COMMAND)


# Excercise from Mosh
# count = 0
# for num in range(1, 10):
#     if (num % 2) == 0:
#         print(num)
#         count += 1
# print(f"the are {count} even numbers")


# functions (Defining a fuction and creating arguements  )

# def greet_em(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")


# greet_em("elliot", "Mashiane")

# activity on control flow

# import random

# secret_number = random.randint(1, 10)

# print("Welcome to the Guess the number Game!")
# print("I'm thinking of a number between 1 and 10")

# attempts = 0

# while True:
#     guess = int(input("Enter your guess: "))
#     attempts += 1

#     if guess == secret_number:
#         print(f"Congratulations! You guessed the correct number! in {
#               attempts} attempts!")
#         break
#     elif guess < secret_number:
#         print("Too Low! Try again.")

#     else:
#         print("Too high! Try again.")


string = "maple"

for item in enumerate(string):
    print(item)
