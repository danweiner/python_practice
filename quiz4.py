# Quiz 4, Part 1

##x = "mississipi" 
##print (x[5:0:-2])
### ssi

##x = "mississipi"
##print (x.replace('s','z',2))
###mizzissipi

##my_str = "PYTHON"
##print (my_str.ljust(8,'x'))
### PYTHONxx

##my_str = "abcdecebacd"
##print (my_str.rfind("c", 3, 10))
### 9

##x = "bye bob"
##print (x.strip("b"))
### ye bo

##x = ["dog", "cat", "pet"]
##print ("ZZ".join(x))
### dogZZcatZZpet

##x = "hello hello"
##print (x.count("h",1,7))
### 1

##x = "Cat Dog"
##print (x.swapcase())
### cAT dOG

##x = "CSE"
##print (x.center(9,"x"))
### xxxCSExxx

##x = "CSE_1309"
##print (x.index("0"))
### 6


# Quiz 4, Part 2 (Count Consonants)

'''Write a function named count_consonants that receives a string as
parameter and returns the total count of the consonants in the string.
Consonants are all the characters in the english alphabet except for
'a', 'e', 'i', 'o', 'u'. If the same consonant repeats multiple times you
should count all of them. Note that capitalization and punctuation does not
matter here i.e. a lower case character should be considered the same as an
upper case character.
'''
##
##def count_consonants(some_string):
##    some_string = some_string.lower().replace(' ', '')
##    vowels = ['a','e','i','o','u']
##    count = 0
##    for char in some_string:
##        if char not in vowels:
##            count = count + 1
##    return count
##
##
##my_string = 'hello there sani'
##print(count_consonants(my_string))


# Quiz 4, Part 3 (Longest Word)

'''Write a function named find_longest_word that receives a string as
parameter and returns the longest word in the string. Assume that the
input to this function is a string of words consisting of alphabetic
characters that are separated by space(s). In case of a tie between some
words return the last one that occurs.
'''

##def find_longest_word(some_string):
##    some_string = some_string.split()
##    longest_word = None
##    max_length = len(some_string[0])
##    # print(max_length)
##    for word in some_string:
##        if len(word) >= max_length:
##            max_length = len(word)
##            longest_word = word
##    return longest_word
##    
##
##my_string = 'hello there sani hi hey hawaii heaven hi ho'
##print(find_longest_word(my_string))


# Quiz 4, Part 4 (Anagrams Test)

'''Write a function named test_for_anagrams that receives two strings as
parameters, both of which consist of alphabetic characters and returns
True if the two strings are anagrams, False otherwise. Two strings are
anagrams if one string can be constructed by rearranging the characters
in the other string using all the characters in the original string exactly
once. For example, the strings "Orchestra" and "Carthorse" are anagrams
because each one can be constructed by rearranging the characters in the
other one using all the characters in one of them exactly once. Note that
capitalization does not matter here i.e. a lower case character can be
considered the same as an upper case character
'''

##def test_for_anagrams(my_string1, my_string2):
##    my_string1 = string1.lower()
##    my_string2 = string2.lower()
##
##    if len(my_string1) != len(my_string2):
##        return False
##    
##    for char in my_string1:
##        if char not in my_string2:
##            return False
##    return True
##    
##
##string1 = "Orchestral"
##string2 = "Carthorsel"
##print(test_for_anagrams(string1, string2))
##
##
##################### Instructor function ###################
##def _are_anagrams_sample_(sample_string1, sample_string2):
##    if sorted(sample_string1.lower()) == sorted(sample_string2.lower()):
##        return True
##    else:
##        return False


# Quiz 4, Part 5 (Encryption)

'''Encryption problem: You and your friend want to encrypt your messages
and you have shared a secret key that is known to just the two of you.
Every character in the character_set is mapped to some other character
in the secret key. For example 'a' is mapped to 'D', 'b' is mapped to
'd', 'c' is mapped to '1' and so forth as shown below:

character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"

Write a function named my_encryption that accepts a string (a message
which will only consist of the characters from the character set) as
function parameter and encrypts that message using the secret_key and
returns it. For example if input to this function (the message that you
want to send) is:

"Lets meet at the usual place at 9 am"

Then your function should should return the encrypted message:

"oABjMWAABMDBMB2AMvjvDPMYPD1AMDBMGMDW"

Note that capitalization does matter here!

'''

def my_encryption(some_string):
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"

    encrypted_message = ''
    for character in some_string:
        index = character_set.find(character)
        encrypted_message = encrypted_message + secret_key[index]

    return encrypted_message
            
    

my_string = "Lets meet at the usual place at 9 am"
print(my_encryption(my_string))

