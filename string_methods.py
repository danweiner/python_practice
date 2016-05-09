##my_str = "Hello"
##print (my_str.islower())
### prints False

##my_str = "Goodbye"
##print (my_str.lower())
### prints goodbye

##my_str = "GoodBye"
##print (my_str.isupper())
### prints False

##my_str = "Hello"
##print (my_str.upper())
### prints HELLO

##my_str = "GoodBye"
##print (my_str.swapcase())
### prints gOODbYE

##my_str = "computer science engineering"
##print (my_str.title())
### prints Computer Science Engineering

##print ("hello".isalpha())
### True

##my_str = "hello there"
##print (my_str.isalpha())
### False

##my_str = "hello12"
##print (my_str.isalpha())
### False

##my_str = "CSE1309"
##print (my_str.isalnum())
### True

##my_str = "CSE-1309"
##print (my_str.isalnum())
### False

##print ("bird".endswith("ir"))
### False

##print ("abcdef".find("e"))
### 4

##x="Mississippi"
##print (x.rfind('si',3))
### 6

##my_string = "knickknack"
##print (my_string.rfind('k',3,-2))
### 5

##my_str='Engineering'
##print (my_str.replace('e','x'))
### Enginxxring

##print ("Mississippi".replace('i','z',2))
### Mzsszssippi

##print ("university".index("iv"))
### 2

##my_str = "this is a test"
##print (my_str.count('s',5))
### 2

##print ('test'.center(10,'x'))
### xxxtestxxx

##my_str = "Hello"
##print (my_str.center(9,'z'))
### zzHellozz

##my_str = "CSE"
##print (my_str.ljust(7,'x'))
### CSExxxx

##my_string = 'hello'
##print (my_string.rjust(8,"A"))
### AAAhello

##x="oops too"
##print (x.strip("o"))
### ps t

##my_str = "oops too"
##print (my_str.lstrip('o'))
### ps too

##my_str = "oops too"
##print (my_str.rstrip('o'))
### oops t

##my_str = "hello hello"
##print (my_str.rstrip('h'))
### hello hello

##print ("NO".join("test"))
### tNOeNOsNOt

##x= "test".join(["A","B","C"])
##print (x)
### AtestBtestC

##x="hello are you there"
##print (x.split())
### ['hello', 'are', 'you', 'there']

##my_str = "hello hello"
##print (my_str.split('l'))
### ['he', '', 'o he', '', 'o']

##my_str='Computer science'
##print (my_str.split ('e'))
### ['Comput', 'r sci', 'nc', '']

##x="frequency of letters"
##print (x.split("e",2))
### ['fr', 'qu', 'ncy of letters']

##x="Mississippi"
##print (x.split("s",3))
### ['Mi', '', 'i', 'sippi']


### Strings Functions Exercise 1 (Leading White Space)
##
##'''Write a function that accepts an input string consisting of alphabetic
##characters and removes all the leading whitespace of the string and returns
##it without using .strip(). For example if:
##
##input_string = "    Hello  "
##
##then your function should return a string such as:
##
##output_string = "Hello  "
##
##'''
##
##def leading_white_space(string):
##    my_index = None
##    for x in range(0, len(string)):
##        if string[x] != ' ':
##            my_index = x
##            break
##    # slice the string from that index to the end
##    new_string = string[my_index::]
##    return new_string
##
##input_string = "    Hello  "
##print(leading_white_space(input_string))


### Strings Functions Exercise 2 (Trailing White Space)
##
##'''Write a function that accepts an input string consisting of
##alphabetic characters and removes all the trailing whitespace of the string
##and returns it without using any .strip() method. For example if:
##
##input_string = "  Hello       "
##
##then your function should return an output string such as:
##
##output_string = "  Hello"
##'''
##
##def trailing_white_space(string):
##    my_index = None
##    i = len(string)
##    while i > 0:
##        if string[i-1] != "8":
##            my_index = i
##            break
##        i = i -1
##    # slice the string from 0 to that index
##    new_string = string[:my_index]
##    return new_string
##
##input_string = "    Hello   "
##print(trailing_white_space(input_string))


### Strings Functions Exercise 3 (Changing Cases)
##
##'''Write a function which accepts an input string and returns a string
##where the case of the characters are changed, i.e. all the uppercase characters
##are changed to lower case and all the lower case characters are changed to
##upper case. The non-alphabetic characters should not be changed. Do NOT use
##the string methods upper(), lower(), or swap().
##'''
##
##################### Sample Solution ###################
##def _my_Swap(s):
##    output_string=""
##    for char in s:
##        if (ord(char)<= 90) and (ord(char)>=65) :
##            x=chr(ord(char)+32)
##            output_string=output_string+x
##        elif (ord(char)<= 122) and (ord(char)>=97):
##            x=chr(ord(char)-32)
##            output_string=output_string+x
##        else:
##            output_string=output_string+char
##    return output_string
##
##my_string = 'Hello 15 Dotty'
##print(_my_Swap(my_string))


# Strings Functions Exercise 4 (Remove All Spaces)

'''Write a function which accepts an input string consisting of alphabetic
characters and spaces and returns the string with all the spaces removed.
Do NOT use any string methods for this problem.
'''

################### Sample Solution ###################
def _remove_spaces_sample_(string):
    out_string = ""
    for x in range(0, len(string)):
        if string[x] != " ":
            out_string = out_string + string[x]
    return out_string

my_string = 'Hello 15 Dotty'
print(_remove_spaces_sample_(my_string))
