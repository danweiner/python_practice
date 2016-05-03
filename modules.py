# Python Modules Exercise 3 (Find Distance between two points)

'''Write a function that finds the distance between two points
and returns it.

The input for this function will be two 1 Dimensional lists that
contain the x,y,z coordinates each. For example if the input lists are:

a = [2, 3, -5] 
b = [4, -3, 12]

Then your function should return their distance such as:

18.138357147217054
'''

from math import sqrt

def calculate_distance(list1, list2):
    distance = sqrt( ((list1[0]-list2[0])**2) +
                     ((list1[1]-list2[1])**2) +
                     ((list1[2]-list2[2])**2))
    return distance

    # could also use zip function here


a = [2, 3, -5] 
b = [4, -3, 12]

print(calculate_distance(a, b))
