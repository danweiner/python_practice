print('hi')

# Branching programs - using conditionals (if statements)
# x = int( raw_input("Enter an integer: "))
# if x%2 == 0:
#   print('')
#   print('Even')
# else:
#   print('')
#   print('Odd')
# print('Done with conditional')


# Nested conditionals
# x = int( raw_input("Enter an integer: "))
# if x%2 == 0:
#   if x%3 == 0:
#     print('Divisible by 2 and 3')
#   else:
#     print('Divisible by 2 and not 3')
# elif x%3 == 0:
#   print('Divisible by 3 and not 2')
# else:
#   print('Not divisible by 2 or 3')


# Using compound Booleans

#x > y and x < z for example


# Iteration (looping)

# This code squares the value of x by repetitive addition (by adding x to itself)
# x = 3
# ans = 0
# itersLeft = x
# while(itersLeft != 0):
#   ans = ans + x
#   itersLeft = itersLeft - 1
# print(str(x) + '*' + str(x) + '=' + str(ans))
# This prints out '3 * 3 = 9'


# Classes of algorithms

# 1 - Guess and Check
# One example of this is Exhaustive Enumeration

# Find the cube root of x using guess and check
# add abs and if statement in else to account for negative inputs
# x = int(raw_input("Enter an integer: "))
# ans = 0
# while ans**3 < abs(x):
#   ans = ans + 1
# if ans**3 != abs(x):
#   print(str(x) + ' is not a perfect cube')
# else:
#   if x < 0:
#     ans = -ans
#   print('Cube root of ' + str(x) + ' is ' + str(ans)) 


# For loops - another way to use guess and check

# Computing cube root using for loops

# x = int(raw_input("Enter an integer: "))
# # Generate
# for ans in range(0, abs(x)+1):
#   # Test / Check
#   if ans**3 == abs(x):
#     break
# if ans**3 != abs(x):
#   print(str(x) + ' is not a perfect cube')
# else:
#   if x < 0:
#     ans = -ans
#   print("Cube root of" + str(x) + ' is ' + str(ans))


# Approximation methods

# Start with exhaustive enumeration
# take small steps to generate guesses in order
# check to see if close enough

# In general it will take x/step size to get to the solution (so it could take a while)
# x = 25
# epsilon = 0.01 # this is how close we want to get
# step = epsilon**2
# numGuesses = 0
# ans = 0.0
# # Check to see that you haven't gone too far and you're not done with the loop yet
# while (abs(ans**2 - x)) >= epsilon and ans <= x:
#   ans += step
#   numGuesses += 1
# print('numGuesses = ' + str(numGuesses))
# if abs(ans**2-x) >= epsilon:
#   print("Failed on square root of " + str(x))
# else:
#   print(str(ans) + ' is close to the square root of ' + str(x))


# Bisection search

# This is a faster search method than approximation
# At each stage, reduce the range of values you need to search by half

# Example of square root problem
# x = 25
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = x
# # Initial answer is the mid point
# ans = (high + low) / 2.0
# # This is asking 'Am I close enough?'
# while abs(ans**2-x) >= epsilon:
#   print('low = ' + str(low) + ' high ' + str(high) + 'ans = ' + str(ans))
#   numGuesses += 1
#   # If guess was too low, you make that low number into the answer
#   if ans**2 < x:
#     low = ans
#   else:
#     high = ans
#   ans = (high + low)/2.0
# print('numGuesses = ' + str(numGuesses))
# print(str(ans) + ' is close to the square root of ' + str(x))

# This takes significantly fewer steps than the approximation method 


# Newton-Raphson algorithm ( For square root  of k --> g - (g**2 - k) / 2g) ) 

# epsilon = 0.01
# y = 800.0
# guess = y/2.0

# while abs(guess*guess - y) >= epsilon:
#   guess = guess - (((guess**2) - y) / (2 * guess))
#   print(guess)
# print('Square root of ' + str(y) + ' is about ' + str(guess))


# Turing Complete Language = numbers, strings, assignments, input/output, comparisons, looping constructs
# We can compute anything with a Turing complete language, but it lacks abstraction
# Functions give us abstraction

# A simple function to return the max of x or y

# def max(x, y):
#   if x > y:
#     print(x)
#   else:
#     print(y)

# # We then have to call the function
# # We can bind the result to a variable

# z = max(3, 4)


# Successive multiplication

# x = float(raw_input('Enter a number: '))
# p = int(raw_input('Enter an integer power: '))

# result = 1

# for turn in range(p):
#   print('iteration: ' + str(turn) + ' current result: ' + str(result))
#   result = result * x

# # Now capture it in a procedure

# def iterativePower(x,p):
#   result = 1
#   for turn in range(p):
#     print('iteration: ' + str(turn) + ' current result: ' + str(result))
#     result = result * x
#   print(result)

# iterativePower(5, 6)


# Variable Binding

# def f(x):
#   y = 1
#   x = x + y
#   print('x = ' + str(x))
#   return x

# x = 3
# y = 2
# z = f(x)
# # Print values are x = 4, z = 4, x = 3, y = 2
# # control reverts to global environment where values of x, y, and z are visible
# print('z = ' + str(z))
# print('x = ' + str(x))
# print('y = ' + str(y))
# each function call creates a new environment


# Another example

# def square(x):
#   return x*x

# def twoPower(x,n):
#   while n>1:
#     x = square(x)
#     n = n/2
#   return x

# x = 5
# n = 1
# print(square(5))
# print(twoPower(2, 8))


# Root Finding Using Bisection Search

# def findRoot1(x,power,epsilon):
#   low = 0
#   high = x
#   ans = (high + low) / 2.0
#   while abs(ans**power - x) > epsilon:
#     if ans**power < x:
#       low = ans
#     else:
#       high = ans
#     ans = (high + low) / 2.0
#   return ans 

# print(findRoot1(25, 2, .001)) 
# print(findRoot1(27, 3, .001))
# # Results in infinite loop
# print(findRoot1(-27, 3, .001))


# Fixing function for negative number
# def findRoot2(x,power,epsilon):
#   if x < 0 and power%2 == 0:
#     return None
#   # can't find even powered root of negative number
#   low = min(0,x)
#   high = max(0,x)
#   ans = (high + low) / 2.0
#   while abs(ans**power - x) > epsilon:
#     if ans**power < x:
#       low = ans
#     else:
#       high = ans
#     ans = (high + low) / 2.0
#   return ans 

# print(findRoot2(25, 2, .001)) 
# print(findRoot2(27, 3, .001))
# print(findRoot2(-27, 3, .001))
# # But this fails
# print(findRoot2(0.25, 2, .001))


# Fixing function for decimal number
# def findRoot3(x,power,epsilon):
#   '''x and epsilon int or float, power an int
#   epsilon > 0 power >= 1
#   returns a float y st y**power is within epsilon of x
#   if such a float does not exist, it returns None
#   '''
#   if x < 0 and power%2 == 0:
#     return None
#   # can't find even powered root of negative number
#   low = min(-1,x)
#   high = max(1,x)
#   ans = (high + low) / 2.0
#   while abs(ans**power - x) > epsilon:
#     if ans**power < x:
#       low = ans
#     else:
#       high = ans
#     ans = (high + low) / 2.0
#   return ans 

# print(findRoot3(25, 2, .001)) 
# print(findRoot3(27, 3, .001))
# print(findRoot3(-27, 3, .001))
# # But this fails
# print(findRoot3(0.25, 2, .001))


# Iterative Algorithms

# Looping constructs are generally iterative algorithms
##capture computation in a set of state variables

# Simple example

# def iterMul(a,b):
#   result = 0
#   while b > 0:
#     result += a
#     b -= 1
#   return result

# print(iterMul(5, 3))


# Recursive Algorithms

# reduce a problem to simpler or smaller versions of same problem
# keep reducing to simpler case that can be solved directly (base case)

# def recurMul(a,b):
#   # Base case
#   if b == 1:
#     return a
#   else:
#     # Recursive step
#     return a + recurMul(a, b-1)

# print(recurMul(5, 3))


# Factorial = The classic recursive problem

# Iterative Factorial

# def factI(n):
#   '''assumes that n is an int > 0
#   returns n!
#   '''
#   res = 1
#   while n > 1:
#     res = res * n
#     n -= 1
#   return res

# def factR(n):
#   '''assumes that n is an int > 0
#   returns n!
#   '''
#   if n == 1:
#     return n
#   return n*factR(n - 1)

# print(factI(3))
# print(factI(5))
# print(factR(3))
# print(factR(5))


# Towers of Hanoi - example of Recursive problem solving

# def printMove(fr, to):
#   print('move from ' + str(fr) + ' to ' + str(to))

# def Towers(n, fr, to, spare):
#   # base case
#   if n == 1:
#     printMove(fr, to)
#   else:
#     Towers(n - 1, fr, spare, to)
#     Towers(1, fr, to, spare)
#     Towers(n - 1, spare, to, fr)


# Towers(1, 'f', 't', 's')
# # This is base case - just says move from f to t

# Towers(2, 'f', 't', 's')
# # This says
# ## Move from f to s (spare)
# ## Move from f to t
# ## Move from s to t

# Towers(5, 'f', 't', 's')

