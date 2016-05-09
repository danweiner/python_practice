# Midterm Exam, Part 1

##x = ["dog", 2, "cat", 34, 5.8]
##m = 0
##for i in range(len(x)):
##    m = m + i
##print(m)
### prints 10

##def my_fun(x,y):
##    m = x ** y  
##y = my_fun(2, 3)    
##print(y)
### prints None

##i = 1
##while False:
##    if i % 5 == 0:
##        break
##    i = i + 2
##print(i)
### prints 1
### if while True - prints 5

##count = 0
##list_1 = []
##for i in range(1,4):
##    list_1.append(i**2)
##for x in list_1:
##    count = count + x
##print(count)
### prints 14

##def my_fun(a):
##    a[0] = 'new value:'     
##    a[1] = a[1] + 1      
##
##x = ['old value:', 99]
##my_fun(x)
##print (x[0], x[1])
### prints new value: 100

##x = [ 2, "dog", 6, 4, "pet", 3, 9, "cat"]
##count = 0
##for item in x:
##    m = 0
##    if item == "pet" or item == 3:
##        m = x.index(item)
##        count = count + m
##print(count)
### prints 9

##count = 0
##my_list = [2, 4, 1, 5, 7, 3, 9, 4]
##new_list = my_list[1:7:2]
##for item in new_list:
##    count = count + 1
##print(count)
### prints 3

##x = 0
##my_list = []
##while x < 10:
##    if x % 2 == 0:
##        my_list.append("dog")
##    elif x % 3 == 0:
##        my_list.remove("dog")
##        
##    print('x is', x, 'my list is', my_list)
##    x = x + 1
##    
##print(my_list.count("dog"))
### prints 3

##def my_fun(x):
##    z = 0
##    for item in x:
##        m = x.count(item)
##        if m > z:
##            z = m
##    return z
##
##y = ["cat", 4, "dog" , "cat" , 2, "cat", 2]
##print (my_fun(y))
### prints 3

##list_1 = ["dog", 3, "cat" , 25, 2.4]
##list_2 = ["car", 25, "dog" , 43]
##count = 0
##for item in list_1:
##    if item in list_2:
##        count = count + 1
##print (count)
### prints 2


# Midterm Exam, Part 2

##my_list = []
##for k in range(1,101,20):
##    my_list.append(k)
##print (my_list[: :2] )
### prints [1, 41, 81]

##def my_fun(x):
##    for k in range (len(x)):
##        x.extend(x[:k])
##        print('k is', k, 'x is', x)
##m = [1,5,3]
##my_fun(m)
##print(m)
### prints [1, 5, 3, 1, 1, 5]

##def my_fun(x):
##    for k in range (len(x)):
##        x.append(x[:k])
##m = [1,5,3]
##my_fun(m)
##print(m)
### prints [1,5,3,[],[1],[1,5]]

##my_list = [9, 8, 7]
##for k in range (3):
##    print(k)
##    my_list.insert(-k, k+1)
##    print('k is', k)
##print(my_list)
### prints [1, 9, 8, 3, 2, 7]

##my_list = [12, "cat", 3.4, "dog", 62]
##new_list = []
##for k in range(5):
##    print('k is', k)
##    if k % 2:
##        m = my_list.pop(k)
##        print('k is', k, 'm is', m)
##        new_list.append(m)
##print(new_list)
### prints ['cat', 62]

##def my_fun(my_list,s,e):
##    del (my_list[s:e])
## 
##values = [2, 9, 16, 3, 24, 13, 15]
##my_fun(values,-6,-4)
##my_fun(values,2,4)
##print(values)
### prints [2, 3, 15]

##def my_fun(i):
##    values = []
##    values.append(i)
##    return values
##my_fun(5)
##print(my_fun(3))
### prints 3

##def my_fun(m):
##    x = []
##    for k in range(len(m)):
##        if m[k] % 3 == 0 and m[k] % 2:
##            x.insert(k, m[k])
##    return x
## 
##values = [2, 9, 16, 3, 24, 13, 15]
##print(my_fun(values))

##def my_fun(m, increment):
##    x = 0
##    while x < len(m):
##        m[x] = m[x] + increment
##        x = x + 1
##    return m 
##
##values = [4, 3, 7]
##print(my_fun(values, 2))
### prints [6, 5, 9]

##def my_fun(m):
##    x = m[:]
##    for k in x:
##        if type(k) == int:
##            m.remove(k)
##            
##values = [3, [3,4], 2.9, 3, 6, 'dog', 5]
##my_fun(values)
##print(values)


### Midterm Exam, Part 3 (Most Divisors)
##
##'''Write a function called find_integer_with_most_divisors
##that accepts a list of integers and returns the integer from
##the list that has the most divisors. In case of a tie, return
##the first item that has the most divisors. For example:
##
##if the list is:
##
## [8, 12, 18, 6]
##
##In this list, 8 has four divisors which are: [1,2,4,8] ;
##12 has six divisors which are: [1,2,3,4,6,12]; 18 has six divisors
##which are: [1,2,3,6,9,18] ; and 6 has four divisors which are: [1,2,3,6].
##Notice that both 12 and 18 are tied for maximum number of divisors
##(both have 6 divisors). Your function should return the first item
##with maximum numer of divisors; so it should return:
##
##12
##'''
##
##def list_of_divisors(list):
##     # first set max_divisors to 0
##    max_divisors = 0
##    max_divisors_item = None
##    for items in list:
##        # create a list to hold the divisors of all items in the list
##        output_list = []
##        for number in range(1, items):
##            # Check for the remainder when k is divided by number
##            # if the remainder is 0 that means number is a divisor of k
##            if items % number == 0:
##                # append number to the output list
##                output_list.append(number)
##        length = len(output_list)
##        # if the length of divisors for a particular element
##        # is greater than the current one i.e max_divisors
##        # then set max_divisors as that length and max_divisor_item as
##        # that particular item
##        if length > max_divisors:
##            max_divisors = length
##            max_divisors_item = items
##    return max_divisors_item
##
##my_list = [8, 12, 18, 6]
##print(list_of_divisors(my_list))


### Midterm Exam, Part 4 (List of Primes)
##
##'''Write a function named list_of_primes that accepts
##a positive integer n and returns a sorted list (ascending order)
##of all the prime numbers between 2 and n (including 2 but not including n)
##'''
##
##def list_of_primes(n):
##    my_list = []
##    integer = 2
##    while integer < n:
##        prime = True
##        start = 2
##        while start < integer:
##            if integer % start == 0:
##                prime = False
##            start = start + 1
##        if prime == True:
##            my_list.append(integer)
##        integer = integer + 1
##    return my_list
##
##print(list_of_primes(8))
##
##
##def list_of_primes_for(n):
##    my_list = []
##    for i in range(2, n):
##        prime = True
##        for j in range(2, i):
##            if i % j == 0:
##                prime = False
##        if prime == True:
##            my_list.append(i)
##    return my_list
##
##print(list_of_primes_for(17))


### Midterm Exam, Part 5 (Items Price)
##
##def items_price(a,b):
##    result = 0
##    for i in range(0, len(a)):
##        result += a[i] * b[i]
##    return result
##    
##
##A = [2, 3, 5, 7, 9]
##B = [5, 8, 4, 1, 11]
##
##print(items_price(A,B))


### Midterm Exam, Part 6 (ListsiL)
##
##'''Write a function named crazy_list that accepts a list as parameter
##and returns a boolean (either True or False) based on whether or not
##the list is the same forward and backwards. You may NOT use list.reverse()
##method. 
##'''
##
##def crazy_list(list):
##    size = len(list)
##    if size % 2 == 0:
##        # if the length is even
##        mid = int(size / 2)
##        first_half = list[0:mid]
##        # get the second half and reverse it
##        second_half = list[mid::][::-1]
##    else:
##        mid = int((size ) / 2)
##         # get the first half
##        first_half = list[0:mid]
##        # get the second half and reverse it
##        second_half = list[mid+1::][::-1]
##    if first_half == second_half:
##        return True
##    else:
##        return False
##    
##my_list = [5, 6, 8, 9, 'PYTHON', 9, 8, 6, 5]
##my_list2 = [4, 5, 6, 7, 8, 4, 5, 2] 
##print(crazy_list(my_list2))


### Midterm Exam, Part 7 (Pattern Sum)
##
##'''Write a function called pattern_sum that receives two single digit positive integers,
##(k and m) as parameters and calculates and returns the total sum as: 
##k + kk + kkk + .... (the last number in the sequence should have m digits) 
##For example, if the two integers are:
##
##(4, 5)
##
##Your function should return the total sum of: 
##4 + 44 + 444 + 4444 + 44444 
##Notice the last number in this sequence has 5 digits. The return value should be:
##
##
##49380
##'''
##
##def pattern_sum(a,b):
##    chain_list = []
##    sum = 0
##    for x in range(1, b+1):
##        chain_list.append(x * str(a))
##    for items in chain_list:
##        sum = sum + int(items)
##
##    return sum
##
##print(pattern_sum(4,5))


### Midterm Exam, Part 8 (Unique Common Elements)
##
##'''Write a function named unique_common that accepts two lists both
##of which contain integers as parameters and returns a sorted list
##(ascending order) which contains unique common elements from both the lists.
##If there are no common elements between the two lists, then your function
##should return the keyword None 
##'''
##
##def _unique_common_elements_sample_ed2_(a, b):
##    common = []
##    for items in a:
##        if items in b:
##            common.append(items)
##    if not common:
##        return None
##
##    unique = []
##    for items in common[:]:
##       if items not in unique:
##           unique.append(items)
##    return sorted(unique)
####    
##    
##    
##my_list1 = [5, 6, -7, 8, 8, 9, 9, 10]
##my_list2 = [2, 4, 8, 8, 5, -7]
##print(_unique_common_elements_sample_ed2_(my_list1, my_list2))


### Midterm Exam, Part 9 (GCD)
##
##'''Write a function named find_gcd that accepts a list of positive integers
##and returns their greatest common divisor (GCD). Your function should return
##1 as the GCD if there are no common factors between the integers. Here are some
##examples:
##
##if the list was
##
##
##[12, 24, 6, 18]
##
##then your function should return the GCD:
##
##6
##'''
##
##def sample_gcd_list_ed2_(my_list):
##    result = my_list[0]
##    print('outer result is', result)
##    for i in range(1, len(my_list)):
##        print('result is', result, 'my_list[i]', my_list[i])
##        result = my_gcd(result, my_list[i])
##        print('another result is', result)
##        
##        
##    return result
##    
##  
##def my_gcd(a,b):
##    while b:
##        print('pre a is', a, 'pre b is', b)
##        a, b = b, a%b
##        print('b is', a, 'a mod b is', b)
##    return a
##    
##
##
##list = [12, 24, 6, 18]
##print(sample_gcd_list_ed2_(list))


# Midterm Exam, Part 10 (Numbers To Words)

'''Write a program that asks the user to enter an integer between
1 and 9999 (both inclusive) and then prints the input integer using words.
For example if the user enters:

3421

Then your program should print

three thousand four hundred twenty one

'''

################### Instructor code ###################
n=int(input('please enter an integer between 1 and 9999: '))

one_to_ten = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

ten_to_nineteen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                    'sixteen', 'seventeen', 'eighteen', 'nineteen']

twenty_to_ninety = ['','','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
'ninety']

temp_str=""
if n==0:
    temp_str='zero'
    #print('zero')
first_digit=n//1000
second_digit=(n%1000)//100
third_digit=(n%100)//10
fourth_digit=(n%10)
if first_digit>0:
    temp_str=temp_str+one_to_ten[first_digit]+' thousand '
    #print (one_to_ten[first_digit],'thousand ',end='')
if second_digit>0:
    temp_str=temp_str+one_to_ten[second_digit]+' hundred '
    #print (one_to_ten[second_digit],'hundred ',end='')
if third_digit>1:
    temp_str=temp_str+twenty_to_ninety[third_digit]+" "
    #print (twenty_to_ninety[third_digit],'',end='')
if third_digit==1:
    temp_str=temp_str+ten_to_nineteen[fourth_digit]+" "
    #print (ten_to_nineteen[fourth_digit],'',end='')
else:
    if fourth_digit:
        temp_str=temp_str+one_to_ten[fourth_digit]+" "
        #print (one_to_ten[fourth_digit],'',end='')
if temp_str[-1]==" ":
    temp_str=temp_str[0:-1]
print (temp_str)


