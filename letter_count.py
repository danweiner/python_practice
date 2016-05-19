def LetterCountI(str): 
  
  # list of words
  words = str.split(" ")
  
  # the table that will contain each word with a key and value pair
  # being the characters and the number of times they appeared
  # e.g. {hello: {h: 1, e: 1, l: 2, o: 1}}
  table = {}
  
  for i in range(0, len(words)):
    
    # create new entry in table with the key 
    # being this word and value is empty dict
    thisWord = words[i]
    table[thisWord] = {}
    
    # create a key/value pair that will store
    # the highest letter count for each word
    table[thisWord]["highest"] = 0
    
    # loop through each character in word and
    # store number of times each letter appears
    for c in range(0, len(words[i])):
      
      # see if this character already exists in table for
      # this word: if so add 1 to the count, if not set count = 1
      thisChar = thisWord[c]
      if thisChar in table[thisWord]:
        table[thisWord][thisChar] += 1
      else:
        table[thisWord][thisChar] = 1
        
      # update the highest letter count for each 
      # new letter in the iteration
      if table[thisWord][thisChar] > table[thisWord]["highest"]:
        table[thisWord]["highest"] = table[thisWord][thisChar]
        
    # setup a new object that will store the word
    # with the highest number of repeating characters
    answer = {"word": '', "count": 1}
    
    # now determine what word has the highest number 
    # of repeating letters by accessing the "highest"
    # property of each word in the table
    for w in table:
      if table[w]["highest"] > answer["count"]:
        answer["count"] = table[w]["highest"]
        answer["word"] = w
      
  if answer["count"] == 1:
    return -1
  else:
    return answer["word"]
 
print(LetterCountI("world hellllllo from coderbyte"))
