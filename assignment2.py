# Part 1: Find mismatch

'''Write a function named find_mismatch that accepts two strings
as input arguments and returns:

    0 if the two strings match exactly.
    1 if the two strings have the same length and mismatch in
    only one character.
    2 if the two strings do not have the same length or mismatch
    in two or more characters.

Capital letters are considered the same as lower case letters.
Here are some examples:


First string	Second String	Function return
Python	Java	2
Hello There	helloothere	1
sin	sink	2 (note not the same length)
dog	Dog	0
'''

##def find_mismatch(s1,s2):
##    if len(s1) != len(s2):
##        return 2
##    s1 = s1.lower()
##    s2 = s2.lower()
##    number_of_mismatches = 0
##    for index in range(len(s1)):
##        if s1[index] != s2[index]:
##            number_of_mismatches += 1
##            if number_of_mismatches > 1:
##                return 2
##    return number_of_mismatches
##    
##
##print(find_mismatch('hellod','hello'))


# Part 2: Find single insertion or deletion

'''Write a function named single_insert_or_delete that accepts two strings as input arguments and returns:

    0 if the two strings match exactly.
    1 if the first string can become the same as the second string by inserting or deleting a single character. Notice that inserting and deleting a character is not the same as replacing a character.
    2 otherwise
Capital letters are considered the same as lower case letters. Here are some examples:

First string	Second String	Function return
Python	Java	2
book	boot	2
sin	sink	1 (Inserting a single character at the end)
dog	Dog	0
'''

def single_insert_or_delete(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if s1 == s2:
        return 0
    if abs(len(s1) - len(s2)) != 1:
        return 2

    if len(s1) > len(s2):
        # only deletion is possible
        for k in range(len(s2)):
            if s1[k] != s2[k]:
                if s1[k+1:]==s2[k:]:
                    return 1
                else:
                    return 2
        return 1

    else: # s1 is shorter and only insertion is possible
        for k in range(s1):
            if s1[k] != s2[k]:
                if s1[k:]==s2[k+1:]:
                    return 1
                else:
                    return 2
        return 1
                



print(single_insert_or_delete('python','java'))
