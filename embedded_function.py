# ''Write a function that accepts two numbers a and b as function parameters, and returns True if
# the sum of the two numbers is an even number, False otherwise.''

# Solving using one function

##def test_even(a,b):
##    # calculate the sum of the two numbers
##    my_sum = a + b
##
##    # then check if the sum is an even number or not
##    if my_sum % 2 == 0:
##        return True
##    else:
##        return False
##
##print(test_even(2,3))


# Solving using embedded functions

def embedded_function(a,b):
    # first find the sum of the two numbers
    my_sum = a + b

    # write a function that accepts a number as a parameter and
    # returns True or False
    def lets_test_for_even(n):
        if n % 2 == 0:
            return True
        else:
            return False

    # call the inner function from within the outer function
    my_result = lets_test_for_even(my_sum)
    return my_result

print(embedded_function(2,3))
    
