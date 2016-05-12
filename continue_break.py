# This program prints every char of the string

##for char in 'computer':
##    print(char)
##    
##print('Finished the loop \n')
##
##
### this shows the use of continue in a for loop
##
##for char in 'computer':
##    if char == 'p':
##        continue
##        # This skips the letter 'p'
##    print(char)
##
##print('Finished the for loop with a continue\n')
##
##
### This program shows the use of a break statement
##
##for char in 'computer':
##    if char == 'p':
##        break
##        # Any characters after 'p' won't be printed
##    print(char)
##
##print('Finished the for loop with a break\n')


##count = 20
##for x in range(0,10):
##    count = count - 1
##    if x == 2:
##        break
##print(count)
### prints out 17

##k = 1
##while k < 5:
##    if k % 7 == 0:
##        break
##    k = k + 2
##print(k)
### prints out 5

##my_list = ['dog', 24, 'cat', 12]
##count = 0
##for element in my_list:
##    if element == 'cat':
##        continue
##    count = count + 1
##print(count)
### Prints out 3

##my_str = 'university'
##count = 0
##for char in my_str:
##    if char == 'i':
##        continue
##    else:
##        count = count + 1
##print(count)
### Prints 8

##my_str = 'university'
##count = 0
##for char in my_str:
##    count = count + 1
##    if char == 'e':
##        break
##print(count)
### Prints 5

my_list = [6, 5, 7, 2, 3, 5, 7, 8]
count = 0
for number in my_list:
    if number == 5 or number == 7:
        continue
    else:
        count = count + number
print(count)
# Prints 19


