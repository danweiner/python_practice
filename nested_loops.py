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

start_number = 2
end_number = 50
current_number = start_number

for current_number in range (start_number, end_number+1):
    is_current_number_prime = True
    for current_divisor in range (2, current_number) :
        if current_number % current_divisor == 0 :
            is_current_number_prime = False
            break
    if is_current_number_prime :
        print(current_number, 'is prime')
    

print('All done')

