##Using a for loop, write a program which prints
##the sum of all the even numbers from 1 to 101.


##sum = 0
##for number in range(1, 102):
##    if number % 2 == 0:
##        sum = sum + number
##print(sum)

##Using a for loop, write a program which asks the user to
##type an integer, n, and then prints the sum of
##all numbers from 1 to n (including both 1 and n).

##n = int(input("Enter a number: "))
##
##sum = 0
##
##for number in range(1, (n + 1)):
##    sum = sum + number
##
##print(sum)


##Using a for loop, write a program which
##asks the user to type an integer, n,
##and then prints the sum of the square of
##all numbers form 1 to n (including both 1 and n).

##n = int(input("Enter a number: "))
##
##sum = 0
##
##for number in range(1, (n + 1)):
##    sum = sum + (number ** 2)
##print(sum)


##Write a program that asks the user for an input
##'n' (assume that the user enters a positive integer)
##and prints a sequence of powers of 10 from 10^0 to 10^n
##in separate lines. For example if 'n' is equal to 4
##then the output should look like the following:
##
##1
##10
##100
##1000
##10000

n = int(input("Enter a number: "))

for number in range(0, (n + 1)):
    print(10**number)


