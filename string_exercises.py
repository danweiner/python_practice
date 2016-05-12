### This function accepts a string as input
### and returns the reverse of the input string
##
##def reverse_string(input_string):
##    output_string = ""
##    for char in input_string:
##        output_string = char + output_string
##    return output_string
##
### main program to test reverse string
##
####test_string = "Hello"
####result_string = reverse_string(test_string)
####print(result_string)
##
##
##def reverse_string_v2(input_string):
##    output_string = ""
##    for k in range(len(input_string)-1, -1, -1):
##        output_string = output_string + input_string[k]
##    return output_string
##
##test_string = "Hello"
##result_string2 = reverse_string_v2(test_string)
##print(result_string2)


### This function finds the number of n letter words in the input string
##
##def find_n_letter_words(input_string, n):
##    words = input_string.split()
##    n_letter_words = 0
##    for word in words:
##        if len(word) == n:
##            n_letter_words = n_letter_words + 1
##    return n_letter_words
##
### Main program to test the find_n_letter_words function
##
##test_string = "he who would learn to fly one day"
##total_words = 0
##for k in range(1,11):
##    x = find_n_letter_words(test_string, k)
##    total_words = total_words + x
##    print('There are', x, 'words with', k, 'characters.')
##print('****\nThere are a total of', total_words, 'words in the string')


### Strings Exercise 1 (Palindrome Test)
##
##'''Write a function that takes a string consisting of alphabetic characters
##as input argument and returns True if the string is a palindrome. A
##palindrome is a string which is the same backward or forward. Note that
##capitalization does not matter here i.e. a lower case character can be
##considered the same as an upper case character.
##'''
##
##def palindrome_test(string):
##    string = string.lower()
##    length = len(string)
##    mid = length//2
##    # print(string[:mid])
##    if length % 2 == 0:
##        print(string[mid:])
##        if string[:mid] == string[mid:][::-1]:
##            return True
##        else: return False
##    elif length % 2:
##        if string[:mid] == string[mid + 1:][::-1]:
##            return True
##        else: return False
##    
##
##print(palindrome_test('Hel0leh'))
##
##
##################### Sample Solution ###################
##def _is_palindrome_sample_(sample_string):
##    # Check if the inverted string  equals the original string
##    if str(sample_string).lower() == str(sample_string)[::-1].lower():
##        return True     # Sample string is a palindrome
##    else:
##        return False    # Sample string is not a palindrome


### Strings Exercise 2 (Sorted Test)
##
##'''Write a function that takes a list of words as an input argument and returns
##True if the list is sorted and returns False otherwise.
##'''
##
##def sorted_test(sample_list):
##    copy = sample_list[:]
##    copy.sort()
##
##    if copy == sample_list:
##        return True
##    else: return False
##
##my_words = ['apple','banana', 'carrot', 'dog', 'hawaii']
##print(sorted_test(my_words))


# Strings Exercise 3 (Vowels Count)

'''Write a function which returns the total number of vowels in an input string
which consists of alphabetic characters. Note that capitalization does not
matter here i.e. a lower case character should be considered the same as an
upper case character. For this problem, the vowels are considered to be
A, E, I, O, U.
'''
##
##def vowels_count(string):
##    string = string.lower()
##    vowels = ['a', 'e', 'i', 'o', 'u']
##    total = 0
##    for char in string:
##        for letter in vowels:
##            if char == letter:
##                total = total + 1
##    return total
##
##my_string = 'hEllo there'
##print(vowels_count(my_string))
##
##
##################### Sample Solution ###################
##def _total_vowels_sample_(sample_string):
##    count = 0
##    sample_string=sample_string.lower()
##    vowels = ['a', 'e', 'i', 'o', 'u']
##    for char in sample_string:
##        if char in vowels:
##            count = count + 1
##    return count


### Strings Exercise 4 (Count Input Character)
##
##'''Write a function that accepts a string and a character as input and returns
##the number of times the character is repeated in the string. Note that
##capitalization does not matter here i.e. a lower case character should be
##treated the same as an upper case character.
##'''
##
##def count_input_char(string, char):
##    string = string.lower()
##    char = char.lower()
##
##    total = 0
##
##    for letter in string:
##        if letter == char:
##            total = total + 1
##
##    return total
##
##
##my_string = 'hEllo there'
##character = 'e'
##print(count_input_char(my_string, character))


### Strings Exercise 5 (Count Words Starting With a Character)
##
##'''Write a function that accepts a string and a character as input and returns
##the count of all the words in the string which start with the given character.
##Assume that capitalization does not matter here. You can assume that the input
##string is a sentence i.e. words are separated by spaces and consists of
##alphabetic characters.
##'''
##
##def counting_starting_words(my_string, x):
##    my_string = my_string.lower()
##    my_string = my_string.split(' ')
##    x = x.lower()
##    #print(string)
##    count = 0
##    for word in my_string:
##        if word[0] == x:
##            count = count + 1
##    return count
##        
##
##
##print(counting_starting_words('hello here hey Hawaii hunt dog', 'd'))


### Strings Exercise 6 (Count Words of a Length)
##
##'''Write a function which returns the number of words in the input string
##which have more than 4 characters. Assume that the input string consists
##of alphabetic characters separated by spaces and capitalization does not
##matter i.e. an upper case character should be treated the same as a lower case
##character.
##'''
##
##def count_words_of_length(string):
##    split_string = string.lower().split(' ')
##    # print(split_string)
##    count = 0
##    for word in split_string:
##        length = len(word)
##        if length > 4:
##            count = count + 1
##    return count
##        
##
##my_string = 'hello hey hi hawaii'
##print(count_words_of_length(my_string))
    

### Strings Exercise 7 (Most Common Character)
##
##'''Write a function that takes a string consisting of alphabetic characters
##as input argument and returns the most common character. Ignore white spaces
##i.e. Do not count any white space as a character. Note that capitalization
##does not matter here i.e. that a lower case character is equal to a upper case
##character. In case of a tie between certain characters return the last
##character that has the most count
##'''
##
##################### Sample Solution ###################
##def _most_common_character_(sample_string):
##    stripped_string = sample_string.replace(" ", "")    # remove all white spaces
##    lowercase_stripped_string = stripped_string.lower()    # convert to lower case
##    sample_character = None
##    sample_maximum_count = 0
##
##    # Iterate through the given string and for each character
##    # set a count, among these counts,  return the character whose count is maximum
##    # On case of tie, return the last character that occurs that has the most count
##    for character in lowercase_stripped_string:
##        each_character_count = lowercase_stripped_string.count(character)
##        if each_character_count >= sample_maximum_count:
##            sample_maximum_count = each_character_count
##            sample_character = character
##    return sample_character


### Strings Exercise 8 (Reversed and Case Swapped)
##
##'''Write a function which accepts an input string and returns a reverse
##of the input string while the case for every single character is reversed.
##The input string for this function would be a sentence (words separated by
##spaces) consisting of alphabetic characters. For example if:
##
##input_string = "Hello Python World"
##
##then the function should return a string such as:
##
##"DLROw NOHTYp OLLEh"
##
##'''
##
##def reverse_and_swap(string):
##    output = ''
##    i = -1
##    # iterate from end to front
##    while i != (- (len(string) + 1)):
##        output = output + string[i].swapcase()
##        i = i - 1
##    return output
##    
##input_string = "Hello Python World"
##print(reverse_and_swap(input_string))
##
##def reverse_and_swap_v2(string):
##    output = ''
##    length = len(string)
##
##    for i in range(-length + 1, -1, -1):
##        output = output + string[i].swapcase()
##
##input_string = "Hello Python World Bison!"
##print(reverse_and_swap(input_string))


# Strings Exercise 9 (Preserve and Reverse)

'''Write a function that accepts a string of words separated by spaces
consisting of alphabetic characters and returns a string such that each
word in the input string is reversed while the order of the words in the
input string is preserved. The length of the input string must be equal
to the length of the output string i.e. there should be no extra trailing
or leading spaces in your output string. For example if:

input_string   = “this is a sample test”

then the function should return a string such as:

"siht si a elpmas tset"


'''
def preserve_and_reverse(string):
    split_string = string.split(' ')
    output_list = []
    for word in split_string:
        word = word[::-1]
        output_list.append(word)

    output_string = ''
    for string in output_list:
        output_string = output_string + string + ' '

    output_string = output_string.strip()
    return(output_string)

input_string = 'this is a sample test'
print(preserve_and_reverse(input_string))



#Sample Solution ###################
def _preserve_and_reverse_sample_(string):
    splitted_list = string.split()
    for x in range(0, len(splitted_list)):
        splitted_list[x] = splitted_list[x][::-1]
    # Initialize an output string
    output_string = ""
    for x in range(0, len(splitted_list)):
        output_string += splitted_list[x] + " "
    # Strip any white spaces
    output_string = output_string.strip()
    return output_string
    


