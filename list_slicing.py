##my_list=['pet', 12, 'cat', 4.3, 'dog', 46]
##print (my_list[0:1])
### prints ['pet']

##my_list=['pet', 12, 'cat', 4.3, 'dog', 46]
##print(my_list[1:3])
### prints [12, 'cat']

##my_list=['pet', 12, 'cat', 4.3, 'dog', 46]
##print(my_list[0:4])
### prints ['pet', 12, 'cat', 4.3]

##my_list=['pet', 12, 'cat', 4.3, 'dog', 46]
##print(my_list[0:6])
### prints ['pet', 12, 'cat', 4.3, 'dog', 46]

##my_list = [5, 'old', 'new', 8, 'time', 2]
##print(my_list[2:4])
### prints ['new', 8]

##my_list = [5, 'old', 'new', 8, 'time', 2]
##print(my_list[0:3])
### prints [5, 'old', 'new']

##my_list = [5, 'old', 'new', 8, 'time', 2]
##print(my_list[3:2])
### prints []

##my_list = [5, 'old', 'new', 8, 'time', 2]
##print(my_list[3:7])
### prints [8, 'time', 2]

##my_list = [5, 'old', 'new', 8, 'time', 2]
##print(my_list[0:1])
### prints [5]


### List Slicing Exercise 3 (Every Other Element)
##
##'''Write a function that accepts a list as input and returns
##a new list which includes every other element in the original list.
##Keep the first element, i.e. input_list[0]. For example if:
##
##input_list = ["we", "love", "python", "so","much"]
##
##then your function should return a list such as:
##
##['we', 'python', 'much']'''
##
##def return_every_other_element(list):
##    my_list = []
##    for item in range(0, len(list)+1, 2):
##        item = list[item]
##        my_list.append(item)
##    return my_list
##
##input_list = ["we", "love", "python", "so","much"]
##print(return_every_other_element(input_list))

##def return_every_other_element(list):
##    my_list = list[::2]
##   
##    return my_list
##
##input_list = ["we", "love", "python", "so","much"]
##print(return_every_other_element(input_list))

##        
##################### Sample Solution ###################
##def _every_other_element_sample_(sample_list):
##    output = []
##    length = len(sample_list)
##    output.append(sample_list[0])
##    for element in range(1, length):
##        if element % 2 == 0:
##            output.append(sample_list[element])
##    return output

##my_list=[54,'cow',0.25,32,'worm']
##print(my_list[0:-2])
### prints [54, 'cow', 0.25]

##my_list=[54,'cow',0.25,32,'worm']
##print(my_list[2:-2])
### prints [0.25]

##my_list=[54,'cow',0.25,32,'worm']
##print(my_list[3:-3])
### prints []

##my_list=[54,'cow',0.25,32,'worm']
##print(my_list[0:-1])
### prints [54, 'cow', 0.25, 32]

##my_list = ['python', 3.4, 54, 'java', 82, 'c', 7.4]
##length = len(my_list)
##print(my_list[0:length:2])
### prints ['python', 54, 82, 7.4]

##my_list = ['python', 3.4, 54, 'java', 82, 'c', 7.4]
##print(my_list[6:0:-2])
### prints [7.4, 82, 54]

##my_list=['python', 3.4, 54, 'java', 82, 'c', 7.4]
##print(my_list[0:-1:3])
### prints ['python', 'java']

##my_list=['python', 3.4, 54, 'java', 82, 'c', 7.4]
##print(my_list[-1:0:-1])
### prints [7.4, 'c', 82, 'java', 54, 3.4]

##my_list=[24, 'car', 'tv', 5.3, 'apple', 36]
##print(my_list[:3])
### prints [24, 'car', 'tv']

##my_list=[24 ,'car', 'tv', 5.3, 'apple', 36]
##print(my_list[2:])
### prints ['tv', 5.3, 'apple', 36]

##my_list=[24, 'car', 'tv', 5.3, 'apple', 36]
##print(my_list[1:3:])
### prints ['car', 'tv']

##my_list=[24, 'car', 'tv', 5.3, 'apple', 36]
##print(my_list[2::3])
### prints ['tv', 36]

##my_list=[24, 'car', 'tv', 5.3, 'apple', 36]
##print(my_list[::2])
### prints [24, 'tv', 'apple']

my_list=[24, 'car', 'tv', 5.3, 'apple', 36]
print(my_list[::])
# prints[24, 'car', 'tv', 5.3, 'apple', 36]
