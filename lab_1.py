#class work

temp = float(input("Enter temperature in Celsius: "))
new_temp = int(((temp*9/5)+32))

print(f"Temperature in Fahrenheit: {new_temp}")

# Example (run in terminal):
first_name = input("Enter customer first name: ")
last_name = input ("Enter customers last name: ")
city = input("Enter customers city: ")

print(f"{first_name} surname is {last_name} and she lives in {city}")

# Lab day 1
# QUESTION 1
order_id = 1001
city = "London"
amount_gbp = 45.50
is_complete = True

print(f"{order_id}\n{city}\n{amount_gbp}\n{is_complete}")

# QUESTION 2

order_id = 1002
city = "Manchester"
amount_gbp = 23.75
is_complete = False

print(f" Order {order_id} from {city} has value {amount_gbp}")


# QUESTION 3
# print(f"Store: {store_name}")
# store_name = "Bristol"

#Correction
store_name = "Bristol"
print(f"Store: {store_name}")

# The first code failed because no name was assigned to the variable store_name before it was used in the print statement. 
# Python reads from top to bottom, so the variable needs to be defined before it can be used.

# QUESTION 4
#B. A variable gives a name to a value that can be reused later.

# QUESTION 5
order_count = 12
average_value = 36.75
store_name = "Leeds"
is_open = True

print(f"{type(order_count)}\n{type(average_value)}\n{type(store_name)}\n{type(is_open)}")

# QUESTION 6
unit_price = 24.50
quantity = 3
delivery_fee = 4.99

# calculate
subtotal = unit_price * quantity
final_total = subtotal + delivery_fee

print(f"{subtotal:.2f}\n{final_total:.2f}")

# QUESTION 7
quantity_text = "4"
price_text = "12.50"
Total = float(quantity_text) * float(price_text)
print(f"{Total:.2f}")

# QUESTION 8
# D. Convert it with float().

# QUESTION 9

amount = int(input("Enter the amount: "))
is_high_value = amount >= 100

print(f"Is high value: {is_high_value}")

# QUESTION 10

# case 1
status = "complete"
amount_gbp = 45.50

print(status == "complete")
print(amount_gbp > 0)

#case 2
print(status == "cancelled")
print(amount_gbp > 45.50)

# case 3
print(status == "complete")
print(amount_gbp == -5.00)

# QUESTION 11

store_name = input("Enter store name: ")
order_amount = float(input("Enter order amount: "))

accepted = order_amount >= 0

print(f"{store_name} order accepted: {accepted}")


# QUESTION 12
# 
# A. True

# QUESTION 13
city = "London"
orders = 8
revenue_gbp = 356.7

print(f"{city}:{orders} orders | Revenue £{revenue_gbp:.2f}")

# QUESTION 14
# A SyntaxError
city = "London"
print(city)

# B NameError
amount = 25
print(amount)

# C TypeError
amount = int("25")
print(amount + 10)

# D ValueError
quantity = int("3")

# QUESTION 15
amount = 125
print(amount)

# QUESTION 16
# C. Convert price to float before multiplying

# QUESTION 17
order_id = int(input("Enter order ID: "))
city = input("Enter city: ")
unit_price = float(input("Enter unit price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount percentage: "))

subtotal = unit_price * quantity
discount_amount = subtotal * (discount_percent / 100)
final_total = subtotal - discount_amount

print(f"{subtotal:.2f}\n{discount_amount:.2f}\n{final_total:.2f}")

# QUESTION 18

quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount: "))

valid_quantity = quantity > 0
valid_discount = 0 <= discount <= 100

all_valid = valid_quantity and valid_discount

print(f"Valid quantity: {valid_quantity}\nValid discount: {valid_discount}\nAll valid: {all_valid}")


# QUESTION 19
city = input("City: ")
amount = float(input("Amount: "))
 
is_high_value = amount >= 100
print(f"{city} | £{amount:.2f} | High value: {is_high_value}")


# QUESTION 20
amount = float(input("Enter amount: "))
is_high_value = amount >= 100

print(f"Amount: £{amount:.2f} | High value: {is_high_value}")