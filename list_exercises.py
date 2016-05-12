### List Manipulation Exercise 1 (Updating a List)
##
##'''Write a function that accepts a list (which has a length of 4 or more)
##and a string and returns the list such that the second through the fourth
##element (index 1 through 3 both inclusive) in the input list are replaced
##by the input string. For example:
##
##input_list = ["Isha", "Chandoygya", "Sri Vasya", "Mandukya", "Sri"]
##input_string = "Brahman"
##
##Then, your function should return a list such as:
##
##['Isha', 'Brahman', 'Brahman', 'Brahman', 'Sri'] '''
##
##def list_update(list, string):
##    for item in range(1, 4):
##        list[item] = string
##    return list
##    
##
##
##input_list = ["Isha", "Chandoygya", "Sri Vasya", "Mandukya", "Sri"]
##input_string = "Brahman"
##
##print(list_update(input_list, input_string))


### List Manipulation Exercise 2 (Extending a List Without List Functions)
##
##'''Write a function that accepts two lists A and B and returns a new list
##which contains all the elements of list A followed by elements of list B.
##Notice that the behaviour of this function is different from list.extend()
##method because the list.extend() method extends the list in place, but here
##you are asked to create a new list and return it. Your function should not
##return the original lists. For example if the input lists are:
##
##A = ['p', 'q', 6, 'k']
##B = [8, 10]
##
##Then your function should return a list such as:
##
##['p', 'q', 6, 'k', 8, 10]
##
##'''
##
##def extend_list(list_a, list_b):
##    my_list = list_a[:]
##    for item in list_b:
##        my_list.append(item)
##
##    return my_list
##
##A = ['p', 'q', 6, 'k']
##B = [8, 10]
##        
##print(extend_list(A, B))
##
##################### Sample Solution ###################
##def _list_manipulation_sample2_(A, B):
##    # In python we can simply implement our
##    # version of list.extend using the '+' operator
##    new_list = A + B
##    return new_list


### List Manipulation Exercise 3 (Sorting a List)
##
##'''Write a function that accepts a list of integers and returns
##a new list which is the sorted version (ascending order) of the original list
##(Original list should not be modified). You may NOT use the built in sort()
##or sorted() functions. Notice that the original list should not be modified
##'''
##
### Sample bubble sort solution
##
##def bubble_sort(original_list):
##    # make a copy of original_list
##    my_list = original_list[:]
##
##    # get the length of the list
##    length = 0
##    for element in my_list:
##        length = length + 1
##
##    unSorted = True
##    while unSorted:
##        unSorted = False
##        for index in range(0, length - 1):
##            # if next element is greater element then swap them
##            if my_list[index] > my_list[index + 1]:
##                temporary_variable = my_list[index]
##                my_list[index] = my_list[index + 1]
##                my_list[index + 1] = temporary_variable
##                unSorted = True
##    return my_list
##
##list = [5,4,6,3,6,4]
##print(bubble_sort(list))


### List Manipulation Exercise 4 (Extending and Sorting)
##
##'''Write a function that accepts two lists both of which contain
##integers and returns a new list which contains all the elements
##from both lists sorted in descending order. Your new list should
##include duplicate elements if they exist. Do NOT use the built
##in sort() or sorted() methods.
##'''
##
##def _merge_and_sort_sample_(a, b):
##    a.extend(b)
##    # Create a new list
##    new_list = []
##    # Loop until a becomes empty
##    
##    while a:
##        # set an arbitrary element as the maximum
##        # in this case we chose the first index
##        maximum = a[0]
##        # loop through the list and
##        # find the element that is largest
##        print('a is', a)
##        print('new list', new_list)
##        for element in a:
##            if element > maximum:
##                maximum = element
##        # append the largest element to the new list
##        new_list.append(maximum)
##        # now remove that largest element from the original list
##        a.remove(maximum)
##    # Ultimately a will become empty
##    # and the loop will end
##    # now return the new list
##    return new_list
##
##A = [1,3,5]
##B = [4,6]
##print(_merge_and_sort_sample_(A, B))


### List Manipulation Exercise 5 (Counting an item in a list)
##
##'''Write a function that accepts a list and a value of
##an element and returns the count of how many times that
##element appears in the list. The behaviour of this function
##should be exactly like the list.count() method. You may NOT
##use any built in list methods for this problem.
##'''
##
##def total_items(list, element):
##    total = 0
##    length = len(list)
##    for item in range(0, length):
##        if list[item] == element:
##            total = total + 1
##    return total
##my_list = [1,2,2,3,3,4,'hello']
##print(total_items(['hello', 22, 333, 3, 'hello', 4, 5, 6], 'hello'))
##
##
##################### Sample Solution ###################
##def _list_manipulation_sample3_(input_list, k):
##    my_Count = 0
##    for element in input_list:
##        if element == k:
##            my_Count = my_Count + 1
##    return my_Count


### List Manipulation Exercise 6 (Extracting a list from a list)
##
##'''Write a function that accepts a list and return a new list
##which contains all but the first and last elements of
##the original list.
##'''
##
##def extract_list(list):
##    new_list = list[1:-1]
##    return new_list
##
##sample_list = [1,2,3,4,5]
##print(extract_list(sample_list))


### List Manipulation Exercise 7 (Modifying a List)
##
##'''Write a function that accepts a list that contains positive
##integers and returns a new list which contains all the elements
##from original list but adds 1 to those elements which are odd.
##For example if :
##
##input_list = [12, 3, 4, 5, 6]
##
##Then your function should return a list such as:
##
##[12, 4, 4, 6, 6]
##
##'''
##
##def modify_list(list):
##    my_list = []
##    for element in list:
##        if element % 2:
##            element = element + 1
##            my_list.append(element)
##        else:
##            my_list.append(element)
##            
##    return my_list
##
##sample_list = [12, 3, 4, 5, 6]
##print(modify_list(sample_list))
##
##
##################### Sample Solution ###################
##def _list_manipulation_sample5_(my_list):
##    input_list = my_list[:]
##    for x in range(0, len(input_list)):
##        if input_list[x] % 2 != 0:
##            input_list[x] = input_list[x] + 1
##    return input_list


### List Manipulation Exercise 8 (Adding Odds from 2 Lists)
##
##'''Write a function that accepts two lists both of which consists
##of integers and returns the total sum of all the odd integers
##from both lists.
##'''
##
##def add_odds(list1, list2):
##    sum = 0
##    list1.extend(list2)
##    for item in list1:
##        if item % 2:
##            sum = sum + item
##    return sum
##
##A = [1,2,3]
##B = [4,5,6]
##
##print(add_odds(A, B))


### List Manipulation Exercise 9 (Unique Elements)
##
##'''Write a function that accepts an input list and returns
##a new list which contains only the unique elements
##(Elements should only appear one time in the list and
##the order of the elements must be preserved as the original list. ).
##'''
##
##def unique_elements(list):
##    my_list = []
##    for items in list:
##        if items not in my_list:
##            my_list.append(items)
##    return my_list
##
##sample = [1,2,2,3,3,4, 'hello']
##print(unique_elements(sample))


### List Manipulation Exercise 10 (Unique Elements From Multiple Lists)
##
##'''Write a function that accepts two input lists and returns
##a new list which contains only the unique elements from
##both lists.
##'''
##
##def unique_elements_multiple(list1, list2):
##    list1.extend(list2)
##    my_list = []
##    for items in list1:
##        if items not in my_list:
##            my_list.append(items)
##    return my_list
##
##sample = [1,2,2,3,3,4, 'hello']
##sample2 = [1,2,3, 'hello', 'there']
##print(unique_elements_multiple(sample, sample2))
##
##
##################### Sample Solution ###################
##def _join_two_lists_unique_sample_(sample_list1, sample_list2):
##    output_list = []
##    for items1 in sample_list1:
##        if items1 not in output_list:
##            output_list.append(items1)
##
##    for items2 in sample_list2:
##        if items2 not in output_list:
##            output_list.append(items2)
##    return output_list


# List Manipulation Exercise 11 (Traversing Backwards)

'''Write a function that accepts a list and returns a new list
such that the new list contains all the items of the old list
in reverse order. Note that this is NOT a sorting problem.
Do NOT use the built in reverse() method for this problem.
For example if:

input_list = ['apples', 'eat', "don't", 'I', 'but',
'Grapes', 'Love', 'I']

then your function should return a list such as:

['I', 'Love', 'Grapes', 'but', 'I', "don't", 'eat', 'apples']

'''

################### Sample Solution ###################
def _reverse_of_a_list_sample_(old_list):
    new_list = []
    length = len(old_list)
    i = -1
    # Iterate the list using negative indices
    while i >= -length:
        new_list.append(old_list[i])
        i = i - 1
    return new_list

input_list = ['apples', 'eat', "don't", 'I', 'but',
'Grapes', 'Love', 'I']

print(_reverse_of_a_list_sample_(input_list))


