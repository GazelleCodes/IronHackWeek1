import numpy as np
 

 
# py_list = [1, 2, 3, 4]
# np_arr = np.array(py_list)
 
# print(type(py_list), type(np_arr))



a = np.array([10, 20, 30])
b = np.zeros(4)
c = np.ones((2, 3))
d = np.arange(0, 10, 2)
 
print(a)
print(b)
print(c)
print(d)




 
# arr = np.array([[10, 20, 30],
#                 [40, 50, 60]])
 
# print(arr[0, 1])   # row 0, col 1
# print(arr[1][2])   # row 1, col 2
# print(arr[-1, -1]) # last row, last col




 
# a = np.array([0,1,2,3,4,5,6,7,8])
# print(a[2:6])      # elements 2,3,4,5
# print(a[:4])       # first four
# print(a[::2])      # every second element
 
# m = a.reshape(3,3)
# print(m)
# print(m[0:2, 1:3]) # first two rows, cols 1 and 2



 
# sales = np.array([120, 75, 300, 45, 200])
# high_sales = sales[sales >= 100]
# print("Original:", sales)
# print("High sales:", high_sales)



 
# a = np.array([10, 20, 30])
# b = np.array([1, 2, 3])
 
# print(a + 5)
# print(a * 2)
# print(a + b)


 
data = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])
 
print("Total sum:", data.sum())
print("Column-wise mean:", data.mean(axis=0))
print("Row-wise max:", data.max(axis=1))
print("Overall min:", np.min(data))

# Class Work

# def multiply_input(x):
#     mult_input = int(x*x)
#     print (mult_input)

# multiply_input(5)

# # this prints
# def add(a,b):
#     sum = a+b
#     return sum
# print(add(5,10))

# # This returns
# def add(a,b):
#     sum = a+b
#     return sum

# add(8,9)



# def area_of_circle(radius):
#     return 3.142 * (radius ** 2)

# def area_of_square(side):
#     return side * side

# def area_of_rectangle(length, width):
#     return length * width


# print("Choose an option to calculate:")
# print("Option1: Cirlcle")
# print("Option2: Square")
# print("Option3: Rectangle")

# Options = input("Enter an Option:")