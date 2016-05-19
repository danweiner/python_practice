##def SecondGreatLow(arr): 
##    arr = sorted(set(arr))
##    print(arr)
##    res = ''
##    if len(arr) < 2:
##        return False
##    elif len(arr) == 2:
##        res = res + str(arr[-1]) + " " + str(arr[0])
##        return res
##    else:
##        res = res + str(arr[1]) + " " + str(arr[-2])
##        return res
### keep this function call here  
##print(SecondGreatLow([180, 45, 45, 45, 15, 10, 10, 10,10]))




##def DivisionStringified(num1,num2):
##
##    # convert the ints to floats
##    # divide and round accordingly
##    div = round(float(num1)/float(num2))
##
##    # convert ans to int then to a str and
##    # finally to a list separating each num
##    div = list(str(int(div)))
##
##    # keep counter for inserting comma logic
##    insert = 0
##
##    # logic for inserting comma into every 3 elements into the reversed list
##    # we use the enumerate function along with reversed function to
##    # loop backwards through the list while maintaining list indices
##    # e.g. ['4', '5', '3', '2'] becomes ['4', ',5', '3', '2']
##    # and then we would join all the nums into a string
##
##    if len(div) > 3:
##        for i, e in reversed(list(enumerate(div))):
##            insert = insert + 1
##            if (insert == 3):
##                div[i] = ',' + e
##                insert = 0
##    # return the elements joined into a proper string
##    return ''.join(div)
##    
### keep this function call here  
##print(DivisionStringified(1400500, 52))


#DivMod

def chocoFeast(n,c,m):
    num_chocos = n//c
    while num_chocos >= m:
        m = m + 1
    return m

print(chocoFeast(6, 2, 2))
