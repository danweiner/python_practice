##x="university" 
##print (x[0:4])
### prints univ

##x="university" 
##print (x[-5:-3])
### prints rs

##x="university" 
##print (x[-5:-2])
### prints rsi

##x="university" 
##print (x[5:0:-2])
### prints rvn

##x = "abcdefg"
##print (x[-5:4])
### prints cd

##x = "abcdefg"
##print (x[5:1:-2]) 
### prints fd

##x = "abcdefg"
##print (x[-6:len(x):2]) 
### prints bdf

##x = "abcdefg"
##print (x[-4:-1:2]) 
### prints df


### Strings, Exercise 3
##
##'''Write a program using while loops that asks the user for a positive integer
##'n' and prints a triangle using numbers from 1 to 'n'. For example if the
##user enters 6 then the output should be like this :
##
##(There should be no spaces between the numbers)
##
##1
##22
##333
##4444
##55555
##666666
##'''
##
##n = int(input('Please enter a number: '))
##
##number = 1
##
##while number <= n:
##    print(str(number) * number)
##    number = number + 1


### Strings Exercise 4
##
##'''Write a program that asks the user for an input 'n' and prints a square
##of n by n asterisks "*". For example if the user enters 5 then the output
##should look like the following: Note that there should be no spaces between
##the asterisks
##
##*****
##*****
##*****
##*****
##*****
##'''
##
##n = int(input('Please enter a number: '))
##
##
##for i in range(1, n+1):
##    print(n * '*')


### Strings Exercise 5
##
##'''Write a program that asks the user for an input 'n'
##(assume that the user enters a positive integer) and prints only
##the boundaries of the triangle using asterisks "*" of height 'n'.
##For example if the user enters 6 then the height of the triangle
##should be 6 as shown below and there should be no spaces between
##the asterisks on the top line:
##
##******
##*   *
##*  *
##* *
##**
##*
##
##'''
##
##n = int(input('Please enter a number: '))
##
##################### Sample Solution ###################
##n = int(input("Please enter a positive integer: "))
##
##if n > 1:
##    print (n*"*") # Print the top line
##    for x in range(n-1, 1, -1):
##        print("*"+ (x-2)*" "+"*") # Print the middle lines
##    print("*") #print the bottom line
##elif n == 1:
##    print("*")


### Character Encoding Exercise 1 (Integer to Character)
##
##'''Write a function that accepts a positive integer n and returns the
##ascii character associated with it.
##'''
##
##def ascii_character(n):
##    character = chr(n)
##    return character
##
##print(ascii_character(1000))


### Character Encoding Exercise 2 (Character to Integer)
##
##'''Write a function that accepts an alphabetic character and returns
##the number associated with it from the ASCII table.
##
##'''
##
##def ascii_number(n):
##    number = ord(n)
##    return number
##
##print(ascii_number('a'))


# Character Encoding Exercise 3 (Sum of Character Code Values)

'''Write a function that accepts an alphabetic string and returns an integer
which is the sum of all the UTF-8 codes of the character in that string.
For example if the input string is "hello" then your function should return 532
'''

def sum_of_letters(n):
    sum = 0
    for characters in n:
        sum = sum + ord(characters)
    return sum

print(sum_of_letters('hello'))

    
