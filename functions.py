

# This function prints parameter input_string when it is called

##def hello(input_string):
##    print('Your input string is: ', input_string)
##
### Prints variable s 4 times
##    
##for k in range(1, 5):
##    print('k is equal to', k)
##    s = 'Dog'
##    hello(s)
    
## 4 categories of functions and parameters
# 1. Nothing goes in, nothing comes out
# 2. Nothing goes in, something comes out
# 3. Something goes in, nothing comes out
# 4. Something goes in, something comes out


# 1. Nothing goes in, nothing comes out

# Doing a task repeatedly and nothing changes - no parameters, no return
# Printing something is not the same as returning something
# Returns 'None' by default

# Example

##def display_message():
##    print('***   PYTHON IS GREAT   ***')
##    print('===========================')
##
### Main Program #
##radius = 5
##print('The radius of the circle is: ', radius)
##display_message() # the function call
##
##circumference = 2*3.14*radius
##print('The circumference of the circle is:', circumference)
##display_message()


# 2. Nothing goes in, something comes out

# Receives no arguments, but does return something

##import random
##
##def report_random():
##    my_number = random.randint(20, 100)
##    return my_number
##
### Main Program #
##
##a = report_random() # return a random int and assign it to a
##print('a is equal to', a)
##b = report_random() # return a random int and assign it to b
##print('b is equal to', b)
##c = report_random() # return a random int and assign it to b
##print('c is equal to',c)


# 3. Something goes in, nothing comes out

# Function receives arguments but does not return anything
# Printing is not returning - return is None

##def calculate_area(length, breadth):
##    area = length * breadth
##    perimeter = 2 * length + 2 * breadth
##    print('area is equal to', area)
##    print('perimeter is equal to', perimeter)

# Main Program #


# 4. Something goes in, something comes out

# Takes some arguments, performs some task, returns some result

##def calculate_area(length, breadth):
##    area = length * breadth
##    perimeter = 2 * length + 2 * breadth
##    my_result = [area, perimeter] # put results in a list
##    return my_result # return the list
##    # return area, perimeter # This would return a tuple
##
### Main Program #
##
##my_list = calculate_area(10, 20) # two arguments are supplied
##print('The resulting list looks like:', my_list)
##
##calculate_area(10, 20)


# Examples of Python Built-In Functions

# abs(x) - returns the absolute value of a number

##my_value = -11.55
##absolute = abs(my_value)
##print('The absolute value is:', absolute)

# len(x) - returns the length of an object, maybe a sequence or collection

##my_list = ['abs', 'len', 1, 2, 'many', 'more to come']
##my_size = len(my_list)
##print('The length of my_list is:', my_size)
##
##print(len('hello'))

# max(iterable, *[, key, default]) - returns largest item of iterable
# max(arg1, arg2 *args[, key]) - returns largest of two or more args

##my_list = [-10, 12, 111, 32.3, 0, 4, 24]
##my_max1 = max(my_list)
##my_max2 = max(my_list[0], my_list[-1])
##print('The largest item of my_list is: ', my_max1)
##print('the larget among the first and last item is', my_max2)


# min() works same way as max()


# sorted(iterable[,key][, reverse])

# - returns a new sorted list from the items in iterable

# Let's sort the following list by the first item in each sub-list

##my_list = [[2,4], [0,13], [11,14], [-14,12], [100,3]]
##
### define a function that specifies what we would like items sorted by
##
##def my_key(item):
##    return item[0]
##
### make the first item in each sub-list our key
##
##new_sorted_list = sorted(my_list, key=my_key)
##
### return a sorted list as specified by our key
##
##print("the sorted list looks like:", new_sorted_list)


# Exercise 1 (Adding 2 Numbers)

# Write a function that accepts a positive integer 'k'
# and adds 5 to it and returns the resulting integer.

##def add_numbers(k):
##    result = k + 5
##    return result
##
##print(add_numbers(10))


# Exercise 2 (Multiplying 2 Integers)

# Write a function that accepts two integers and
# calculates their product and returns it.

##def multiply_numbers(a,b):
##    product = a * b
##    return product
##
##print(multiply_numbers(2,3))


# Exercise 3 (Area of Rectangle)

# Write a function that accepts two positive integers which
# are the height and width of a rectangle and returns a list
# that contains the area and perimeter of that rectangle.

##def dimensions_of_rectangle(length, width):
##    area = length * width
##    perimeter = 2 * (length + width)
##    output_list = [area, perimeter]
##    return output_list
##
##print(dimensions_of_rectangle(20,10))


# Exercise 4 (Area of Circle)

# Write a function that a accepts a positive number 'r' as the
# radius of a circle and calculates and returns the area
# of the circle. Use the value of pi as 3.14

##def area_of_circle(r):
##    area = (r**2)*3.14
##    return area
##
##print(area_of_circle(5))

# Calculate square root function

# Original program - Turn it into a function

##user_response = input('Enter a number: ')
##number = float(user_response)
##guess = number/2
##accuracy = 0.00001
##while abs(number-(guess**2)) > accuracy:
##    guess = (guess+(number/guess))/2
##print(guess)

##def my_square_root(input_number):
##    square_root = input_number/2
##    accuracy = 0.001
##    while abs(input_number-(square_root**2)) > accuracy:
##        square_root = (square_root+(input_number/square_root))/2
##    return square_root
##
##print(my_square_root(16))
##
### This is the main program to check the my_square_root function
##
##for x in range(1,21):
##    y = my_square_root(x)
##    print('Square root of', x, 'is', y)


# Functions Exercise 5 (Sum of a List)

'''Write a function that accepts a list of integers
and returns the sum of all the numbers in the list.
Assume that the input list contains only numbers. Do
NOT use the built-in sum() function.'''

##def sum_of_list(list):
##    sum = 0
##    for item in list:
##        sum = sum + item
##    return sum
##
##my_list = [1,2,3,4]
##
##print(sum_of_list(my_list))


# Functions Exercise 6 (Average of a List)

'''Write a function that accepts a list of integers and
returns the average. Assume that the input list contains
only numbers. Do NOT use the built-in sum() function.'''


##def average_of_list(list):
##    sum = 0
##    length = len(list)
##    for item in list:
##        sum = sum + item
##    average = sum / length
##    return average
##
##my_list = [1,2,3,4,5]
##
##print(average_of_list(my_list))


# Functions Exercise 7 (Maximum of a List)

'''Write a function which accepts an input list of numbers
and returns the largest number in the list
(Do not use python's built-in max() function).'''

##def max_in_list(list):
##    # set the first element of the list as the max
##    max = list[0]
##    for item in list:
##        if item > max:
##            max = item
##    return max
##
##my_list = [1,2,3,-10, 5,6]
##
##print(max_in_list(my_list))


# Functions Exercise 8 (Minimum of a List)

'''Write a function which accepts an input list
of numbers and returns the smallest number in the list
(Do not use python's built-in min() function).'''

##def min_in_list(list):
##    # set the first element of the list as the max
##    min = list[0]
##    for item in list:
##        if item < min:
##            min = item
##    return min
##
##my_list = [1,2,3,-10, 5,6]
##
##print(min_in_list(my_list))


# Functions Exercise 9 (Evaluate an Expression)

'''Write a function that accepts a number x and evaluates
the following expression: (x**4) - (12x**3) + (13x**2) + 11
and returns the value of y'''

##def evaluate_expression(x):
##    y = x**4 - 12*x**3 + 13*x**2 + 11
##    return y
##
##print(evaluate_expression(5))


##def test(x):
##    a = 7
##
### Main Program
##print(test(5))
##
### Prints 'None'

##def my_fun(a):
##    return a*2
##
### Main Program
##print(my_fun(2) + my_fun(3))
##
### Prints 10

##def my_fun(a):
##    return a*2
##
### Main program
##
##print(my_fun(my_fun(2)))

# Prints 8


# Functions Exercise 11 (Magnitude of a Vector)


'''Write a function that finds the magnitude of a given vector.
The magnitude of a vector is the square root of sum of squares
of all the components of the vector. Your input for this function
will be a (vector with x,y,z components) 1 dimensional list
containing 3 integers. For example if the input list is:
vector = [2, 3, -4]
Then you should return the magnitude (as a floating point number)
of this vector:
5.385164807134504'''

##def mag_of_vector(vector):
        # Find sum of squares
##    sum = 0
##    for item in vector:
##        sum = sum + item*item
##
        # Find square root of sum of squares
##    square_root = sum/2
##    accuracy = 0.001
##    while abs(sum-(square_root**2)) > accuracy:
##        square_root = (square_root+(sum/square_root))/2
##    return square_root
##
##vector = [2,3,-4]
##
##print(mag_of_vector(vector))

################### Sample Solution ###################
##def _magnitude_of_a_vector_sample_(vector):
##    x = vector[0]
##    y = vector[1]
##    z = vector[2]
##    mag = ((x**2) + (y**2) + (z**2))**(1/2)
# normalize the vector by dividing each component with the magnitude
##    new_x = x/mag
##    new_y = y/mag
##    new_z = z/mag
##    unit_vector = [new_x, new_y, new_z]
##    return unit_vector


# Functions Exercise 12 (Normalizing a Vector)

'''Write a function that normalizes a vector (finds the unit vector).
A vector can be normalized by dividing each individual component
of the vector by its magnitude. Your input for this function will
be a vector i.e. 1 dimensional list containing 3 integers.
For example if the input list is:
vector = [2, 3, -4]
Then you should return the unit vector(1-Dimensional list) such as:
[0.3713906763541037, 0.5570860145311556, -0.7427813527082074]'''

def mag_of_vector(vector):
        # Find sum of squares
    sum = 0
    for item in vector:
        sum = sum + item*item

        # Find square root of sum of squares
    square_root = sum/2
    accuracy = 0.001
    while abs(sum-(square_root**2)) > accuracy:
        square_root = (square_root+(sum/square_root))/2
        
        # divide each item in vector list by sq rt and append to unit_vector list
    unit_vector = []
    for item in vector:
        item = item / square_root
        unit_vector.append(item)
        
    return unit_vector

vector = [2,3,-4]

print(mag_of_vector(vector))

################### Sample Solution ###################
##def _magnitude_of_a_vector_sample_(vector):
##    x = vector[0]
##    y = vector[1]
##    z = vector[2]
##    mag = ((x**2) + (y**2) + (z**2))**(1/2)
# normalize the vector by dividing each component with the magnitude
##    new_x = x/mag
##    new_y = y/mag
##    new_z = z/mag
##    unit_vector = [new_x, new_y, new_z]
##    return unit_vector
