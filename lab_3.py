

# 1. Write a Python program that asks the user for their name, age, and city, then displays the information in a meaningful sentence.
# def user_info():
#     name = input("What is your name?")
#     age = input ("How old are you?")
#     city = input("Where do live?")
#     return name , age ,city
# name, age, city = user_info()
# print(f"My name is {name}, I am {age} years old and I live in {city}.")

# 2. Write a program that asks the user for two numbers and displays their addition, subtraction, multiplication, and division.
# def calculate_numbers():
#     num1 = int(input("Input a number:"))
#     num2 = int(input("Input a second number:"))

#     Addition = num1 + num2
#     Subtraction = num1 - num2
#     Multiplication = num1 * num2
#     Division = num1/num2

#     return Addition, Subtraction, Multiplication, Division


# Addition, Subtraction, Multiplication, Division = calculate_numbers()
# print(f"{Addition}\n {Subtraction}\n {Multiplication}\n {Division}")

# 3. Write a program to calculate the area of a rectangle. Ask the user to enter the length and width.
# def area_of_rectangle():
#     length = int(input("Enter length:"))
#     Width = int(input("Enter width:"))
#     Area = length * Width
#     return Area

# Area = area_of_rectangle()
# print(f"The area is {Area} m²")

# 4. Write a program that accepts a temperature in Celsius and converts it to Fahrenheit.
# def convert_temp():
#     temp_cel = int(input("Enter temperature in celcius:"))
#     far = (temp_cel * 9/5) + 32
#     return far

# far = convert_temp()
# print(f"The temperature in is {far} °F")

# 5. Write a program that asks the user for a number and determines whether it is positive, negative, or zero.
# def positive_num():
#     num = int(input("Enter a number:"))
#     if num >= 0:
#         is_positive = f"{num} is positive"

#         return is_positive
#     else:
#         return f"{num} is not positive"

# number = positive_num()
# print(f"Number:{number}")

# 6. Write a program that asks the user for a number and determines whether it is even or odd.
# def even_or_odd_num():
#     num = int(input("Enter a number:"))
#     if num  % 2 == 0:
#         is_even = f"{num} is even number"
#         return is_even
#     else:
#         return f"{num} is odd number"
# number = even_or_odd_num()

# print(f" The number {number}")

# 7. Write a program that asks for a person's age and determines whether they are a child, teenager, or adult.
# def determine_age():
#     age = int(input("Enter your age:"))

#     if age >= 18:
#         return f"You are an Adult"
#     elif age in range(13,17):
#         return f"You are a Teenager"
#     else:
#         return f"You are a Child"

# age_bracket = determine_age()
# print(f"{age_bracket}")

#8 Write a program that accepts marks from 0 to 100 and displays the appropriate grade:
# def marks():
#     grade = int(input("Enter grade:"))
#     if grade >= 90 and grade <= 100:
#         return f"A"
#     elif grade >= 80 and grade <= 89:
#         return f"B"
#     elif grade >= 70 and grade <= 79:
#         return f"C"
#     elif grade >= 60 and grade <= 69:
#         return f"D"
#     elif grade < 60:
#         return f"F"
#     else:
#         return f"Invalid grade"

# grades = marks()
# print(f"{grades}")

#9. Write a program that asks for three numbers and finds the largest number.
# 
#10. Write a simple calculator. Ask the user for two numbers and an operator (+, -, *, /) and perform the selected calculation.
def calculator():
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second  number:"))
    choice = input("Enter an operator:")

    if choice == "+":
        return num1 + num2
    elif choice == "-":
        return num1 - num2
    elif choice == "*":
        return num1 * num2
    elif choice == "/":
        return num1/num2
    else:
        return f"invalid operation"

new_calculator = calculator()
print(f"{new_calculator}")