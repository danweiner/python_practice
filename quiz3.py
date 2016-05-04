##count = 0
##for x in range(2,5):
##    count = count + x
##print(count)
### prints 9

##k = 10
##while k > 2:
##    x = k / 2
##    k = k - 1
##print(x)
### prints 1.5

##count = 10
##for x in range(0,7):
##    count = count + 2
##    if x == 4:
##        break
##print(count)
# prints 20

##k = 1
##count = 0
##while count < 10:
##    if k % 4 == 0:
##        break
##    count = count + k
##    k = k + 1
##print(count)
### prints 6

##my_list = ["pet", "dog", 35, "cat", 23]
##count = 0
##for item in my_list:
##    if type(item) == str:
##        continue
##    count = count + 1
##print(count)
### prints 2

##m = 0
##my_str = 'mississipi'
##for char in my_str:
##    if char == 's':
##        continue
##    if char == 'p':
##        break
##    m = m + 1
##print(m)
### prints 4

##m = 0
##for x in range(4,6):
##    for y in range(2,4):
##        m = m + x + y
##print(m)
### prints 28

##m = 0
##x = 1
##while x < 5:
##    print('outer m is', m)
##    y = 1
##    print('outer y is', y)
##    print('x is is', x)
##    while y < 4:
##        
##        m = m + y
##        y = y + 3
##        print('y is', y)
##        print('inner m is', m)
##    x = x + 2
##print(m)
### prints 2

##m = 0
##my_list_1 = [1,2,5]
##my_list_2 = [1,3,2,6,5]
##for x in my_list_1:
##    for y in my_list_2:
##        if x == y:
##            m = m + 1
##print(m)
### prints 3

##m = 0
##my_str_1 = 'cat'
##my_str_2 = 'pet'
##for char_1 in my_str_1:
##    for char_2 in my_str_2:
##        if char_1 != char_2:
##            m = m + 1
##print(m)

##def say_hello():
##    print('Hello World!')
##say_hello()
### prints Hello World!

##def func(x):
##    x = 2
##    print('x is', x)
##func(50)
### prints x is 2

##def even(x):
##    if x % 2 == 0:
##        return x
##    else:
##        return x + 1
##print(even(3))
# prints 4

##def cube(x):
##    return x * x * x
##y = cube(3)
##print(y)
### prints 27

##def fun(x,y,z):
##    z = x * y
##    return x + y + z
##print(fun(2,30))
### prints TypeError

##def find_max(a,b):
##    if a > b:
##        print(a, 'is maximum')
##    elif a == b:
##        print(a, 'is equal to', b)
##    else:
##        print(b, 'is maximum')
##find_max(3,4)
# prints 4 is maximum

##def my_fun(x):
##    count = 0
##    for str in x:
##        if str == 'cat':
##            count = count + 1
##        elif str == 'dog':
##            count = count - 1
##    return count
##z = ['cat', 2, 'cat', 'dog', 34, 'cat']
##print(my_fun(z))
### prints 2

##def myFun():
##    count = 0
##    for x in range(0,3):
##        count = count + x
##    return
##print(myFun())
### prints None

##def fun1(x,y):
##    z = multiply(x,y)
##    m = x + z
##    return m
##
##def multiply(a,b):
##    n = a * b
##    return n
##
##x = 2
##y = 4
##z = fun1(x,y)
##print(x,y,z)
### prints 2 4 10

##def my_fun(x):
##    for m in range(0,3):
##        n = 2
##        while n <= 4:
##            if m == n:
##                x = x + 1
##            n = n + 1
##    return x
##print(my_fun(5))
### prints 6


### Quiz 3, Part 3
##
##'''Write a program that asks the user for a positive number
##'n' as input. Assume that the user enters a number greater
##than or equal to 3 and print a triangle as described below.
##For example if the user enters 6 then the output should be:
##*
##**
##***
##****
##*****
##******
##*****
##****
##***
##**
##*
##
##'''
##
##n = int(input('Please enter a number of stars: '))
##for x in range(1, n+1):
##    print('*' * x)
##for y in range(n-1,0,-1):
##    print('*' * y)
##


### Quiz 3, Part 4
##
##'''Write a function that accepts a list of integers as parameter.
##Your function should return the sum of all the odd numbers in the list.
##If there are no odd numbers in the list, your function should return
##0 as the sum. 
##'''
##
##def sum_of_odd(list):
##    print('list is', list)
##    sum = 0
##    for number in list:
##        print('number is', number)
##        if number % 2:
##            sum = sum + number
##    return sum
##
##my_list = [2,4]
##print(sum_of_odd(my_list))


### Quiz 3, Part 5
##
##'''Write a function that receives a positive integer
##as function parameter and returns True if the integer
##is a perfect number, False otherwise. A perfect number
##is a number whose sum of the all the divisors (excluding itself)
##is equal to itself. For example: divisors of 6 (excluding 6 are) :
##1, 2, 3 and their sum is 1+2+3 = 6.
##Therefore, 6 is a perfect number.
##'''
##def perfect_number_sample(n):
##    sum = 0
##    divisors = []
##    for number in range(1,n):
##        # check for remainder when n is divided by number
##        # if remainder is 0 that means number is divisor of n
##        if n % number == 0:
##            sum = sum + number
##            divisors.append(number)
##            
##    print('Divisors are', divisors)
##    # check if the sum of the divisors is equal to n itself
##    if sum == n:
##        return True
##    else:
##        return False
##
##print(perfect_number_sample(10))


### Quiz 3, Part 6
##
##'''Write a function that accepts a positive integer n
##as function parameter and returns True if n is a prime number,
##False otherwise. Note that zero and one are not prime numbers
##and two is the only prime number that is even. '''
##
##def check_prime(n):
##    if n < 2:
##        return False
##    # iterate from 2 to the number
##    for i in range(2,n):
##        if n % i == 0:
##            return False
##    return True
##
##print(check_prime(7))


### Quiz 3, Part 7
##
##'''Write a function that accepts two positive integers
##as function parameters and returns their least common multiple (LCM).
##The LCM of two integers a and b is the smallest (non zero) positive integer
##that is divisible by both a and b. For example, the LCM of 4 and 6 is 12,
##the LCM of 10 and 5 is 10. '''
##
##def least_common_multiple(a,b):
##    # make a back-up of a
##    copy_of_a = a
##    # while remaander when a is divided by b is not 0
##    # continue to add a to its back-up(copy_of_a)
##    while copy_of_a % b :
##        copy_of_a = copy_of_a + a
##    return copy_of_a
##
##print(least_common_multiple(2,5))


### Quiz 3, Part 8
##
##'''Write a function that accepts two positive integers as parameters.
##The first integer is the number of heads and the second integer is
##the number of legs of all the creatures in a farm which consists of
##chickens and dogs. Your function should calculate and return the number
##of chickens and number of dogs in the farm in a list as specified below.
##If it is impossible to determine the correct number of chickens and dogs
##with the given information then your function should return None.
##Example 1, if your function received the following numbers:
##5, 12
##This means that someone has counted a total of 5 heads and total
##of 12 legs in the farm. Now, your function should calculate how many
##chickens and how many dogs are in the farm and return that information
##in a list exactly as shown below.
##[4, 1]
##this means that there were 4 chickens and 1 dog in the farm.'''
##
##def animals_on_farm(heads, legs):
##    dogs = (legs - heads*2) / 2
##    if dogs < 0 or dogs %1:
##        return None
##    dogs = int(dogs)
##    chickens = heads - dogs
##    if chickens < 0:
##        return None
##    return [chickens, dogs]
##
##print(animals_on_farm(7,12))

## Answers from MIT OCW

# Solve using Enumerate and Check - Brute Force

##def solve(legs, heads):
##    for chickens in range(0, heads + 1):
##        dogs = heads - chickens
##        totLegs = 4*dogs + 2*chickens
##        if totLegs == legs:
##            return [dogs, chickens]
##    return [None, None]
##
##def animals_on_farm():
##    heads = int(input('Enter number of heads: '))
##    legs = int(input('Enter number of legs: '))
##    # This is modularity - suppressing details of 'solve'
##    dogs, chickens = solve(legs, heads)
##    if dogs == None:
##        print('There is no solution')
##    else:
##        print('Number of dogs: ', dogs)
##        print('Number of chickens: ', chickens)
##
### What if it's an underconstraint problem - What if there are spiders on the farm
##
##def solve1(legs, heads):
##    for spiders in range(0, heads + 1):
##        for chickens in range(0, heads - spiders + 1):
##            dogs = heads - chickens - spiders
##            totLegs = 4*dogs + 2*chickens + 8*spiders
##            if totLegs == legs:
##                return [dogs, chickens, spiders]
##    return [None, None, None]
##
##def animals_on_farm1():
##    heads = int(input('Enter number of heads: '))
##    legs = int(input('Enter number of legs: '))
##    # This is modularity - suppressing details of 'solve'
##    dogs, chickens, spiders = solve1(legs, heads)
##    if dogs == None:
##        print('There is no solution')
##    else:
##        print('Number of dogs: ', dogs)
##        print('Number of chickens: ', chickens)
##        print('Number of spiders: ', spiders)
##        
### Print out all solutions - Generalize the loop
##
##def solve2(legs, heads):
##    solutionFound = False
##    for spiders in range(0, heads + 1):
##        for chickens in range(0, heads - spiders + 1):
##            dogs = heads - chickens - spiders
##            totLegs = 4*dogs + 2*chickens + 8*spiders
##            if totLegs == legs:
##                print('Number of dogs: ', dogs)
##                print('Number of chickens: ', chickens)
##                print('Number of spiders: ', spiders)
##                solutionFound = True
##    if not solutionFound: print('There is no solution.')
##
##
##def animals_on_farm2():
##    heads = int(input('Enter number of heads: '))
##    legs = int(input('Enter number of legs: '))
##    # This is modularity - suppressing details of 'solve'
##    dogs, chickens, spiders = solve2(legs, heads)
        
        
    
