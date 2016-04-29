##number_of_cookies = int(input("How many cookies in the jar? "))
##cookies_eaten = 0
##while number_of_cookies > 0:
##    number_of_cookies = number_of_cookies - 1
##    cookies_eaten = cookies_eaten + 1
##    print("Eating cookie number", cookies_eaten)
##print("I ate all the cookies")

# Babylonian algorithm for square root


##number = float(input("Enter a number: "))
##guess = number / 2
##accuracy = 0.001
##iteration = 0
##while abs(number-(guess**2)) > accuracy:
##    print("Iteration", iteration, "Guessed square root is:", guess)
##    guess = (guess + (number/guess))/2
##    iteration = iteration + 1
##print("Original number is", number)
##print("Square root is", guess)


##Write a program which prints the sum of numbers from 1 to 101
##( 1 and 101 are included) that are divisible by 5 (Use while loop)


##sum = 0
##number = 101
##while number > 0:
##    number = number - 1
##    if number % 5 == 0:
##        sum = sum + number
##print(sum) 
##
##x=0
##count=0
##while x <= 101:
##    if x%5==0:
##        count = count+x
##    x=x+1
##print(count)


##Write a program using while loop, which asks the user to type
##a positive integer, n, and then prints the factorial of n.
##A factorial is defined as the product of all the numbers
##from 1 to n (1 and n inclusive)

##x = int(input("Enter a number: "))
##
##y = 1
##factorial = 1
##
##while y <= x:
##    factorial = factorial * y
##    y = y + 1
##print(factorial)


##Write a program using while loop, which prints the sum
##of every third numbers from 1 to 1001 ( both 1 and 1001 are included)

x = 1
sum = 0

while x < 1001:
    sum = sum + x
    x = x + 3
print(sum)
