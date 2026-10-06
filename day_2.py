# number = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")
# # odd or even

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")

# # calculator
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# choice = input("Enter an operation: ")

# addition = num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2
# division = num1 / num2

# if choice == "addition":
#     print(f"{num1} + {num2} = {addition}")
# elif choice == "subtraction":
#     print(f"{num1} - {num2} = {subtraction}")
# elif choice == "multiplication":
#     print(f"{num1} * {num2} = {multiplication}")
# elif choice == "division":
#     print(f"{num1} / {num2} = {division}")
# else:
#     print("Invalid operation")


# even numbers in a loop

# sum = 0
# for i in range(1, 21):
#     if i %2 == 0:
#         sum += i
# print(f"There are {sum} even numbers between 1 and 20.")

# sum = 0
# for i in range(2, 21, 2):
#         sum += i
# print(f"There are {sum} even numbers between 1 and 20.")


# # Temperature conversion
# # celsius = float(input("Enter temperature in Celsius: "))
# # fahrenheit = (celsius * 9/5) + 32

# list_of_temperatures = [0, 10, 20, 30, 40, 50]
# for celsius in list_of_temperatures:
#     fahrenheit = (celsius * 9/5) + 32
#     print(f"{celsius}°C = {fahrenheit:.2f}°F")
# # Using append to create a new list of converted temperatures
# list_cel = [23.3, 23.1, 22.2]
# list_far = []
# for i in list_cel:
#     list_far.append((i * 9 / 5) + 32)
# print(list_far)

# #Using list comprehension to create a new list of converted temperatures
# list_cel= [23.4 , 34.5, 45.5, 56.5]
# list_fah= [temp * 9/5 + 32 for temp in list_cel]
# print(f"Temperature in Fahrenheit: {list_fah}")


# #Calculate salary after tax
# salary = float(input("Enter your salary: "))


# if salary > 50000:
#     tax_rate = 0.2
# if salary >= 35000 and salary <= 50000:
#     tax_rate = 0.15
# if salary < 35000:
#     tax_rate = 0.12

# tax_amount = salary * tax_rate
# salary_after_tax = salary - tax_amount

# print(f"Salary after tax: {salary_after_tax:.2f}")


# # list
# orders = [100, 200.4,"list", True, 500]

# print(orders[0])

# set
unique_orders = {100, 200.4, "list", True, 500}
print(unique_orders)