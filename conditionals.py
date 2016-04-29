##user_input = input("Enter a temp: ")
##
##celsius = float(user_input)
##fahrenheit = (celsius * (9 / 5) ) + 32
##
##if fahrenheit >= 90:
##    print("it's hot")
##else:
##    print("it's not hot")
##print(fahrenheit)

##user_input = input("Enter a word: ")
##if 'dog' in user_input:
##    print('Yes')
##else:
##    print('No')

##user_input = input('Enter a number: ')
##number = int(user_input)
##
##if number % 3 == 0:
##    print('Yes')
##else:
##    print('No')

##user_input = input("Enter a temp: ")
##
##celsius = float(user_input)
##fahrenheit = (celsius * (9 / 5) ) + 32
##print("The temperature is", fahrenheit, "degrees Fahrenheit")
##if fahrenheit < 32:
##    print("it is freezing")
##elif fahrenheit < 50:
##    print("it is chilly")
##elif fahrenheit < 90:
##    print("it is OK")
##else:
##    print("it's hot")

##if 6/2:
##    print('three')
##elif 5:
##    print('five')
##else:
##    print('zero')
### Prints three

##if False:
##    print('false')
##elif 2**3 == 8:
##    print('true')
##else:
##    print('none')
### Prints true

##x = 100
##if x > 10:
##    x = x + 10
##if x > 20:
##    x = x + 50
##print(x)
###Prints 160

##user_input = input("Enter a phrase: ")
##if ('dog') in user_input:
##    print('Dog')
##elif 'cat' in user_input:
##    print('Cat')
##else:
##    print('None')

##age = int(input('Enter your age: '))
##if age <= 0:
##    print('UNBORN')
##elif age <= 150:
##    print('ALIVE')
##else:
##    print('VAMPIRE')

##integer = int(input("Enter a positive number: "))
##if (integer % 2 == 0) and (integer % 3 == 0):
##    print("BOTH")
##elif(integer % 2 == 0) or (integer % 3 == 0):
##    print("ONE")
##else:
##    print("NEITHER")

##Write a program which asks the user to enter an integer 'n'
##which would be the total numbers of hours the user worked in
##a week and calculates and prints the total amount of money
##the user made during that week. If the user enters any
##number less than 0 or greater than 168 (n < 0 or n > 168)
##then your program should print INVALID

##hours_worked = int(input("Enter a hours worked: "))
##
##total_salary = 0
##if hours_worked < 0 or hours_worked > 168:
##    print("INVALID")
##elif hours_worked <= 40:
##    total_salary = hours_worked * 8
##    print("You made $", total_salary, "dollars this week")
##elif hours_worked <= 50:
##    total_salary = (40 * 8) + ((hours_worked - 40) * 9)
##    print("You made $", total_salary, "dollars this week")
##else:
##    total_salary = (40 * 8) + (10 * 9) + ((hours_worked - 50) * 10)
##    print("You made $", total_salary, "dollars this week")
##

##Write a program that asks the user to enter a positive integer n.
##Assuming that this integer is in seconds, your program should convert
##the number of seconds into days, hours, minutes, and seconds and prints
##them exactly in the format specified below. Here are a few sample runs o
##f what your program is supposed to do:

number_of_seconds = int(input("Enter a number of seconds: "))

# Calculate the days
days = number_of_seconds//(24*60*60)
seconds_1 = number_of_seconds % (24*60*60) # Remaining seconds after we get days


# Calculate hours

hours = seconds_1//(60*60) # Get the hours out of seconds_1
seconds_2 = seconds_1 % (60 * 60) # remaining seconds after we get hours


# Calculate the minutes
minutes = seconds_2//60


# Calculate the seconds after minutes

seconds = seconds_2 % 60


print(days, "days", hours, "hours", minutes, "minutes", seconds, "seconds")
    
