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


def ABCheck(str): 
    str = str.replace(' ', '')
    for i in range(0, len(str)):
        if str[i] == 'a' and str[i+3] == 'b':
            return 'true'
    return 'false'
    # code goes here 
    
# keep this function call here  
print(ABCheck("123adzvb"))

