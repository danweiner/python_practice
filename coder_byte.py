##def LetterChanges(str): 
##
##    # code goes here
##    new_str = ''
##    for char in str:
##        if char == ' ':
##            new_str = new_str + ' '
##        elif (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char)<= 122):
##            char = (chr(ord(char) + 1))
##            new_str = new_str + char
##        else:
##            new_str = new_str + char
##    print(new_str)
##    vowels = 'aeiou'
##    for char in new_str:
##        if char in vowels:
##            print(char)
##            new_char = char.upper()
##            print(new_char)
##            new_str = new_str.replace(char, new_char)
##    return new_str
##        
##    
### keep this function call here  
##print(LetterChanges('Hello world!!'))


##def LongestWord(sen): 
##    sen = sen.split()
##    # code goes here
##    max_word = sen[0]
##    max_len = len(max_word)
##    for word in sen:
##        letter_count = 0
##        for char in word:
##            if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char)<= 122):
##                letter_count += 1
##        if letter_count > max_len:
##            max_len = letter_count
##            max_word = word
##    return max_word
##    
### keep this function call here  
##print(LongestWord('hell worlds i am here to rock!!!!!!!'))


##def SimpleSymbols(str): 
##    str = '=' + str + '='
##    length = len(str)
##    for i in range(0, length):
##        if str[i].isalpha():
##            if (str[i-1] != '+') or (str[i+1]!= '+'):
##                return 'false'
##    # code goes here 
##    return 'true'
##    
### keep this function call here  
##print(SimpleSymbols("+f++d+"))


##def TimeConvert(num): 
##    num_hours = num//60
##    num_minutes = num % 60
##    # code goes here 
##    return str(num_hours) + ':' + str(num_minutes)
##    
### keep this function call here  
##print(TimeConvert(45))


##def AlphabetSoup(str): 
##    # code goes here
##    chars = list(str)
##    sorted_chars = sorted(chars)
##    print(sorted_chars)
##    return ''.join(sorted(str))
##    
### keep this function call here  
##print(AlphabetSoup("coderbyte"))


##def SimpleSymbols(str):
##    str = '=' + str + '='
##    str = str.lower()
##    str = list(str)
##    for i in range(0, len(str)):
##        if str[i].isalpha():
##            if (str[i-1] != '+') or (str[i+1] != '+') :
##                return 'false'
##    return 'true'
##    
### keep this function call here  
##print(SimpleSymbols("+D+=3=+s+"))


##def ABCheck(str): 
##    str = str.replace(' ', '')
##    for i in range(0, len(str)):
##        if str[i] == 'a' and str[i+3] == 'b':
##            return 'true'
##    return 'false'
##    # code goes here 
##    
### keep this function call here  
##print(ABCheck("123adzvb"))
##
#########Sample Solution######
##def ABCheck(str): 
##
##  # convert the whole string to lowercase letters
##  str = str.lower()
##
##  # loop through the string
##  for i in range(0, len(str)):
##    
##    # check for "a...b" but we can't go out of bounds on the 
##    # list or an error will be thrown
##    if (str[i] == 'a' and i+4 < len(str) and str[i+4] == 'b'):
##      return 'true'
##
##    # check for "b...a"
##    if (str[i] == 'b' and i+4 < len(str) and str[i+4] == 'a'):
##      return 'true'
##
##  # if none of above were encountered
##  # then return false by default
##  return 'false'
##    
##print ABCheck("Laura sobs")  
##
##
##
##def Palindrome(str): 
##    length = len(str)
##    mid = length//2
##    if length % 2 == 0:
##        str_first = str[:mid]
##        str_second = str[mid:][::-1]
##        if str_first == str_second:
##            return 'true'
##    if length % 2:
##        str_first = str[:mid]
##        str_second = str[mid+1:][::-1]
##        if str_first == str_second:
##            return 'true'
##        
##    return 'false'
##    
### keep this function call here  
##print(Palindrome("nev3ven77"))

##def Palindrome(str): 
##
##  # first we'll get rid of spaces and make the characters 
##  # all lowercase to make it easier to work with
##  str = "".join(str.split(" ")).lower()
##
##
##  # we wrote this reverse code in a previous solution
##  rev = ''.join(reversed(str))
##  print(rev)
##
##  # now it's very easy to check if a string is a palindrome
##  if str == rev:
##    return "true"
##  else:
##    return "false"
##    
##print(Palindrome("Never odd or even"))


##def ArithGeo(arr):
##    
##    # this function will loop through the array
##    # check to see if the difference provided matches
##    # every element pair differenc in the array
##
##    def arrayDiffs(diff, arr, subtract):
##        
##        # loop starting at i = 2 and check if difference is the same
##        for i in range(2, len(arr)):
##
##            # store the temporary difference
##            if subtract:
##                tempDiff = arr[i] - arr[i-1]
##            else:
##                tempDiff = arr[i] / arr[i-1]
##
##            # if the differences do not match return false
##
##            if (tempDiff != diff):
##                return False
##
##            # if we reach the end of the array and all differences matched
##            # return True
##            elif (i == len(arr)-1 and tempDiff == diff):
##                return True
##
##    # store the first difference for a potential arithmetic sequence
##    diffArith = arr[1] - arr[0]
##
##    # store the first difference for a potential geometric sequence
##    diffGeo = arr[1] / arr[0]
##
##    # check the whole array for an arithmetic sequence
##
##    isArithSeq = arrayDiffs(diffArith, arr, True)
##
##    if isArithSeq:
##        return 'Arithmetic'
##
##    # if not an arithmetic sequence, check for geometric sequence
##    else:
##        isGeoSeq = arrayDiffs(diffGeo, arr, False)
##        if isGeoSeq:
##            return 'Geometric'
##        else:
##            return -1
##
##print(ArithGeo([1, 3, 9, 27]))
##        
##    
### keep this function call here  
##print(ArithGeo([5,10,15,20, 25, 31]))


# subset sum problem

def ArrayAdditionI(arr):
    arr = sorted(arr)
    max_num = arr[-1]
    arr = arr[:-1]
    return 'true' if subsetsum(max_num, arr) else 'false'

def subsetsum(max_num, arr):
    if len(arr) == 0:
        return max_num == 0
    return subsetsum(max_num, arr[1:]) or subsetsum(max_num - arr[0], arr[1:])
    
# keep this function call here  
print(ArrayAdditionI([5,7,14,1,2]))






