# Midterm Exam, Part 1

##x = ["dog", 2, "cat", 34, 5.8]
##m = 0
##for i in range(len(x)):
##    m = m + i
##print(m)
### prints 10

##def my_fun(x,y):
##    m = x ** y  
##y = my_fun(2, 3)    
##print(y)
### prints None

##i = 1
##while False:
##    if i % 5 == 0:
##        break
##    i = i + 2
##print(i)
### prints 1
### if while True - prints 5

##count = 0
##list_1 = []
##for i in range(1,4):
##    list_1.append(i**2)
##for x in list_1:
##    count = count + x
##print(count)
### prints 14

##def my_fun(a):
##    a[0] = 'new value:'     
##    a[1] = a[1] + 1      
##
##x = ['old value:', 99]
##my_fun(x)
##print (x[0], x[1])
### prints new value: 100

##x = [ 2, "dog", 6, 4, "pet", 3, 9, "cat"]
##count = 0
##for item in x:
##    m = 0
##    if item == "pet" or item == 3:
##        m = x.index(item)
##        count = count + m
##print(count)
### prints 9

##count = 0
##my_list = [2, 4, 1, 5, 7, 3, 9, 4]
##new_list = my_list[1:7:2]
##for item in new_list:
##    count = count + 1
##print(count)
### prints 3

##x = 0
##my_list = []
##while x < 10:
##    if x % 2 == 0:
##        my_list.append("dog")
##    elif x % 3 == 0:
##        my_list.remove("dog")
##        
##    print('x is', x, 'my list is', my_list)
##    x = x + 1
##    
##print(my_list.count("dog"))
### prints 3

def my_fun(x):
    z = 0
    for item in x:
        m = x.count(item)
        if m > z:
            z = m
    return z

y = ["cat", 4, "dog" , "cat" , 2, "cat", 2]
print (my_fun(y))


