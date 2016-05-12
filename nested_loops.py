# Algorithm to determine if a number is prime

#1. Select a number
#2. Select a divisor and set it equal to 2
#3. Assume the number is prime
#4. If divisor is less than the number go to step 5 else go to step 8
#5. If remainer of number/divisor is zero then number is not prime (exit/stop)
#6. Add one to the divisor
#7. Go to step 4
#8. Number is prime


# A program to determine if a number is prime

##current_number = 24
##current_divisor = 2
##is_current_number_prime = True
##while (current_divisor < current_number) :
##    if current_number % current_divisor == 0 :
##        is_current_number_prime = False
##        break
##    current_divisor = current_divisor + 1
##if is_current_number_prime :
##    print(current_number, 'is prime')
##else:
##    print(current_number, 'is NOT prime')
##print('All done')


# A program to print all the prime numbers between 2 and 50 using nested while loops

##start_number = 100
##end_number = 200
##current_number = start_number
##
##while current_number <= end_number:
##    current_divisor = 2
##    is_current_number_prime = True
##    while (current_divisor < current_number) :
##        if current_number % current_divisor == 0 :
##            is_current_number_prime = False
##            break
##        current_divisor = current_divisor + 1
##    if is_current_number_prime :
##        print(current_number, 'is prime')
##    current_number = current_number + 1
##
##print('All done')


# A program to print all the prime numbers between 2 and 50 using nested for loops

##start_number = 2
##end_number = 50
##current_number = start_number
##
##for current_number in range (start_number, end_number+1):
##    is_current_number_prime = True
##    for current_divisor in range (2, current_number) :
##        if current_number % current_divisor == 0 :
##            is_current_number_prime = False
##            break
##    if is_current_number_prime :
##        print(current_number, 'is prime')
##    
##
##print('All done')

##m = 0
##for x in range(1, 4):
##    for y in range(1,3):
##         m = m + 1
##print(m)
### prints 6


##m = 0
##for x in range(1, 3):
##    for y in range(4,6):
##        m = m + x + y
##print(m)
### prints 24

##m = 0
##for x in range(1,3):
##    k = 0
##    print('m is', m)
##    for y in range(-2, 0):
##        k = k + y
##        m = m + k
##        print('k is', k)
##print(m)
### prints -10

##k = 0
##for x in range(1,3):
##    for y in range(-2, 0):
##        k = k + y
##print(k)
# prints -6

##m = 0
##for x in [3,5,3]:
##    print('m is', m)
##    for y in range(10,11):
##        m = m + x + y
##        print('nested m is', m)
##print(m)
### prints 41

##m = 0
##x = 1
##while x < 4:
##    y = 1
##    print('outer m is', m)
##    while y < 3:
##        m = m + x + y
##        print('y is', y)
##        y = y + 1
##        print('x is', x, 'inner m is', m)
##    x = x + 1
##print(m)
### prints 21

##m = 0
##x = 1
##while x < 4:
##    y = 1
##    print('x is', x)
##    print('outer m is', m)
##    while y < 5:
##        m = m + y
##        print('y is', y)
##        y = y + 1
##        if x + y == 5:
##            break
##        print('inner m is', m)
##    x = x + 1
##print(m)
### prints 10

##m = 0
##x = 10
##while x > 8:
##    print('x is', x)
##    print('outer m is', m)
##    for y in range(1,3):
##        m = m + 1
##        print('y is', y)
##        print('inner m is', m)
##    x = x -1
##print(m)
### prints 4


##m = 1
##for x in [1,2,3]:
##    for y in [3,1,4]:
##        if x == y:
##            m = m * x
##print(m)
### prints 3


##m = 1
##my_list_1 = [2,4,1]
##for x in my_list_1:
##    print('outer m is', m)
##    print('x is', x)
##    for y in range(1,3):
##        print('y is', y)
##        if (x+y) % 3:
##            m = m * x
##            print('inner m is', m)
##print(m)
### prints 8


##m = 0
##my_str_1 = 'university'
##my_str_2 = 'mississipy'
##for char_1 in my_str_1:
##    for char_2 in my_str_2:
##        if char_1 == char_2:
##            m = m + 1
##print(m)
### prints 11
