##MyList = [3, 'dog', 9, 'cat']
##print(len(MyList))
### prints 4

##my_list = ['two', 5, ['one', 2]]
##print(len(my_list))
### prints 3

##MyList = ['pet' , 'dog' ,5, 'cat', 'good','dog']
##print(MyList.count('dog'))
### prints 2

##MyList = ['pet' , 'dog' ,5, 'cat', 'good','dog']
##x = MyList.count('car')
##print(x)
### prints 0

##my_list = [4, 'two' , 'one' ,5,3,2,'bye']
##print (my_list.index('one'))
### prints 2

##MyList = ['pet' , 'dog' ,5, 'cat', 'good','dog']
##print (MyList.index(5))
### prints 2

##MyList = ['pet' , 'dog' ,5, 'cat', 'good','dog']
##print (MyList.index('dog'))
### prints 1

##MyList = ['pet' , 'dog' ,5, 'cat', 'good','dog']
##print (MyList.index('car'))
### Error

##MyList = [1, 5, 67, 3, 4]
##x = MyList.sort()
##print (x)
### prints None

##MyList = [3, 7, 9, 0, 4]
##MyList.sort()
##print (MyList)
### prints [0, 3, 4, 7, 9]

##MyList = ['cow', 'cat', 'dog', 'pet']
##MyList.sort()
##print (MyList)
### prints ['cat', 'cow', 'dog', 'pet']

##MyList = [3, "dog", 9, "cat"]
##MyList.extend([7,8])
##print (MyList)
### prints [3, 'dog', 9, 'cat', 7, 8]

##MyList = ['dog',3]
##MyList.extend('cat')
##print (MyList)
### prints ['dog', 3, 'c', 'a', 't']

##MyList = ['pet' , 'dog' ,5]
##MyList.append('cat')
##print(MyList)
### prints ['pet', 'dog', 5, 'cat']

##my_list = ['two' , 'one' ,5,3,2,'bye']
##my_list.append (['one',2])
##print(my_list)
### prints ['two', 'one', 5, 3, 2, 'bye', ['one', 2]]

##my_list=[1,'dog',2.3]
##my_list.insert(2,'cat')
##print(my_list)
### prints [1, 'dog', 'cat', 2.3]

##MyList = [3, "dog", 9, "cat"]
##MyList.insert(1, [6, 9])
##print (MyList)
### prints [3, [6, 9], 'dog', 9, 'cat']

##MyList = [3, "dog", 9, "cat"]
##MyList.remove(3)
##print (MyList)
### prints ['dog', 9, 'cat']

##MyList = [3, "dog", 9, "cat"]
##MyList.pop()
##print (MyList)
### prints [3, 'dog', 9] 

##MyList = [3, "dog", 0, "cat"]
##del MyList[0]
##print (MyList)
### prints ['dog', 0, 'cat']

##MyList = [3, "dog", 9, "cat"]
##print(MyList.extend([7,8]))
### prints None

##MyList = ['pet' , 'dog' ,5]
##print (MyList.append('cat'))
### prints None

##MyList = ['pet' , 'dog' ,5]
##MyList.append('cat')
##print(MyList)
### prints None

##my_list=[1,"dog",2.3]
##print(my_list.insert(2,"pet"))
### prints None

##my_list = ['two' , 'one' ,5,3,2,'bye']
##print (my_list.remove('one'))
### prints None

##MyList = ['pet' , 'dog' ,1]
##print (MyList.pop(1))
### prints dog

##MyList = ['pet' , 'dog' ,5]
##print (MyList.pop('dog'))
### Error

##my_list = []
##for x in range(2,11,3):
##    my_list.append(x)
##print(my_list)
### prints [2, 5, 8]

##my_list = []
##for x in range(4,30,3.0):
##    my_list.append(x)
##print(my_list)
### Error

##a = range(3,20,4)
##b = []
##for k in a:
##    if k % 2:
##        b.append(k)
##print (b)
### prints [3, 7, 11, 15, 19]

##my_list = []
##for x in range(1,10):
##    if not (x % 3):
##        my_list.append(x)
##print(my_list)
### prints [3, 6, 9]


### List Methods Exercise 7 (List of Multiples)
##
##'''Write a function that accepts a positive integer k
##and returns a list that contains the first five multiples of k.
##The multiples should be calculated starting from 1 to 5
##(including both 1 and 5). For example the first five multiples
##of 3 are 3, 6, 9, 12, and 15'''
##
##def multiples(k):
##    multiples = []
##    for i in range(1,6):
##        multiple = k * i
##        multiples.append(multiple)
##    return multiples
##
##print(multiples(3))


### List Methods Exercise 8 (List of Even Numbers)
##
##'''Write a function that accepts two positive integers a and b
##and returns a list of all the even numbers between a and b
##(including a and not including b).'''
##        
##def list_of_evens(a,b):
##    my_list = []
##    for number in range(a,b):
##        if number % 2 == 0:
##            my_list.append(number)
##    return my_list
##
##print(list_of_evens(1,5))


### List Methods Exercise 9 (List of Odd Numbers)
##
##'''Write a function that accepts two positive integers a and b
##(a is smaller than b)and returns a list that contains all the
##odd numbers between a and b (including a and including b if applicable)
##in descending order.'''
##
##def list_of_odds(a,b):
##    my_list = []
##    for number in range(a,b+1):
##        if number % 2:
##            my_list.append(number)
##    my_list.reverse()
##    return my_list
##
##print(list_of_odds(1,6))
##
##################### Sample Solution ###################
##def _list_of_odd_numbers_sample_(a, b):
##    output_list = []
##    number = b
##    while number >= a:
##        if number % 2 != 0:
##            output_list.append(number)
##        number = number - 1
##    return output_list


### List Methods Exercise 10 (List of Cube Roots))
##
##'''Write a function that accepts a positive integer k and returns
##the ascending sorted list of cube root values of all the numbers
##from 1 to k (including 1 and not including k).
##[if k is 1, your program should return an empty list]'''
##
##def list_of_cube_roots(k):
##    my_list = []
##    for i in range(1,k):
##        if k == 1:
##            break
##        else:
##           cube_root = i **(1/3.0)
##           my_list.append(cube_root)
##           
##    return my_list
##
##print(list_of_cube_roots(1))
##
##################### Sample Solution ###################
##def _list_of_cubes_sample_(k):
##    output_list = []
##    for i in range(1, k):
##        # calculate the cube root
##        cube_root = i**(1/3)
##        output_list.append(cube_root)
##    return output_list
##
##print(_list_of_cubes_sample_(1))


### List Methods Exercise 11 (List of Divisors)
##
##'''Write a function that accepts a positive integer k
##and returns the list of all the divisors of k. Your list
##should include both 1 and k.'''
##
##def list_of_divisors(k):
##    divisors = []
##    for i in range(1,k+1):
##        if k % i == 0:
##            divisors.append(i)
##    return divisors
##
##print(list_of_divisors(6))


