# for loop - finite set of elements
## for c in range(1,10):

# while <condition> - executes as long as a statement is true
## useful when you don't know how many times you dont need to execute code


# Example code - Find the cube root of a perfect cube

x = int(raw_input('Enter an integer: '))
ans = 0
# This avoids an infinite loop
while ans*ans*ans < abs(x):
  ans = ans + 1
  # print 'current guess = ', ans

if ans*ans*ans != abs(x):
  print x, 'is not a perfect cube'

# This converts answer back to negative for a negative input (converted to abs at beginning)
elif x < 0:
  print('You entered a negative number')
  ans = -ans
print 'Cube root of ' + str(x) + ' is ' + str(ans)


# FizzBuzz

# Write a program that prints numbers from 1 - 100
# For multiples of 3 print "Fizz" instead of the number
# for multiples of 5 print "Buzz" instead of the number
# For multiples of 3 and 5 print "FizzBuzz"

for i in range(1, 101):
  # Get the string value of a number
  s = str(i)
  if i % 3 == 0 or i % 5 == 0:
    s = ''
    if i % 3 == 0:
      s = s + 'Fizz'
    if i % 5 == 0:
      s = s + 'Buzz'
  print s
