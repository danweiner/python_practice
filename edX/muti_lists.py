# Example of multidimensional list
# my_course = [['Buny', 90, 87, 95],['Duck', 78, 96, 89],
#              ['Rubb', 83, 85, 92]]
# for student_data in my_course:
#     total_grade = 0
#     for grade_index in range(1, len(student_data)):
#        total_grade = total_grade + student_data[grade_index]
#     print('The average grade for', student_data[0], 'is',
#           total_grade/3.0)

# Multidimensional Lists Exercise 1 (Sum of a 2-D List)

'''
Write a function which accepts a 2D list of numbers and
 returns the sum of all the number in the list You can assume
 that the number of columns in each row is the same.
 (Do not use python's built-in sum() function).
'''

# def sum_of_two_d_list(two_list):
#     total = 0
#     count = 0
#     for one_list in two_list:
#         for number in range(0, len(one_list)):
#             total = total + one_list[number]
#             count = count + 1
#     print(count)
#     return total
#
# ################### Sample Solution ###################
# def _sum_of_a_2d_list_sample_(sample_2d_list):
#     # Initialize total sum to be 0
#     total_SUM = 0
#     # Get the length of rows and columns
#     number_of_rows = len(sample_2d_list)
#     number_of_columns = len(sample_2d_list[0])
#     # Initialize row index to 0
#     rows = 0
#     # Produce row indices 0, 1, 2, ...number_of_rows
#     while rows < number_of_rows:
#         # for each row, initialize the column index to 0
#         columns = 0
#         # Produce column indices 0, 1, 2, ... number_of_columns
#         while columns < number_of_columns:
#             # Added the element i.e. list[row][column] to total sum
#             total_SUM = total_SUM + sample_2d_list[rows][columns]
#             # Increment to the next column index
#             columns = columns + 1
#         # increment to the next row index
#         rows = rows + 1
#     # Finally return the total sum
#     return total_SUM



# my_list = [[90, 87, 95], [78, 96, 89],
#             [83, 85, 92]]
# print(sum_of_two_d_list(my_list))

# def average_of_two_list(two_list):
#     total = 0
#     count = 0
#     for one_list in two_list:
#         for number in range(0, len(one_list)):
#             total = total + one_list[number]
#             count += 1
#     return total/count
#
#
# my_list = [[90, 87, 95], [78, 96, 89],
#             [83, 85, 92]]
# print(average_of_two_list(my_list))
#
# ################### Sample Solution ###################
# def _average_of_a_2d_list_sample_(sample_2d_list):
#     # Initialize total sum to be 0
#     total_sum = 0
#     number_of_items=0
#     # Get the length of rows and columns
#     for row_index in range(len(sample_2d_list)):
#         for col_index in range(len(sample_2d_list[row_index])):
#             total_sum=total_sum+sample_2d_list[row_index][col_index]
#             number_of_items=number_of_items+1
#     return total_sum/number_of_items

# Multidimensional Lists Exercise 3 (Maximum Even Value of a 2-D List)

'''Write a function that accepts a 2D list of integers and
 returns the maximum EVEN value for the entire list. You can
 assume that the number of columns in each row is the same.
 Your function should return None if the list is empty or all
  the numbers in the 2D list are odd. Do NOT use python's built
   in max() function.
'''

# def max_even_value(two_list):
#     if not two_list: # list is empty
#         return None
#     max_val = None
#     for row in two_list:
#         row_max = max_even_of_1d_list(row)
#         if row_max:
#             if max_val == None or row_max > max_val:
#                 max_val = row_max
#     return max_val
#
# def max_even_of_1d_list(input_list):
#     max_val = None
#     for element in input_list:
#         if element % 2 == 0: # if element is even
#             if max_val == None or element > max_val:
#                 max_val = element
#     return max_val
#
#
# my_list = [[90, 87, 95], [78, 91, 89],
#              [83, 85, 92]]
# print(max_even_value(my_list))


# Multidimensional Lists Exercise 4 (List of Sum of Rows of a 2-D List)

'''Write a function that takes a two-dimensional list
 (list of lists) of numbers as argument and returns a list
 which includes the sum of each row. You can assume that
 the number of columns in each row is the same.
'''
# def list_sum_of_rows(two_d_list):
#     row_total = []
#     for row in two_d_list:
#         total = 0
#         for number in range(0, len(row)):
#             total = total + row[number]
#         row_total.append(total)
#     return row_total
#
#
# my_list = [[90, 87, 95], [78, 91, 89],
#              [83, 85, 92]]
# print(list_sum_of_rows(my_list))
#
# ################### Sample Solution ###################
# def _sum_of_rows_sample_(sample_list):
#     mylist = []
#     for item in sample_list:
#         mylist.append(sum(item))
#     return mylist


# Multidimensional Lists Exercise 5 (List of Sum of Columns of a 2-D List)

'''Write a function that takes a two-dimensional list
(list of lists) of numbers as argument and returns a list which
includes the sum of each column. Assume that the number of columns
in each row is the same.
'''
################### Sample Solution ###################
# def _sum_of_columns_sample_(sample_list):
#     # Solution type 1:
#     # return [max(col) for col in zip(*sample_list)]
#     # Alternative Solution
#     cols = len(sample_list[0])
#     mylist = []
#     for c in range(cols):
#         # iterating over each column
#         column_sum = 0
#         for row in sample_list:
#             print(row[c])
#             column_sum += row[c]
#         mylist.append(column_sum)
#     return mylist
#
# my_list = [[90, 87, 95], [78, 91, 89],
#              [83, 85, 92]]

#print(_sum_of_columns_sample_(my_list))


# Multidimensional Lists Exercise 6 (Count Rows with Even and Odd Sums)

'''Write a function that will receive a 2D list of integers. The
function should return the count of how many rows of the list have
 even sums and the count of how many rows have odd sums. For
 example if the even count was 2, and odd count was 4 your function
  should return them in a list like this: [2, 4].
'''
# def count_odd_even_rows(sample_list):
#     result = []
#     odd_total = 0
#     even_total = 0
#     for row in sample_list:
#         total = 0
#         for number in range(len(row)):
#             total = total + row[number]
#         if total % 2 == 0:
#             even_total += 1
#         elif total % 2:
#             odd_total += 1
#     result.append(even_total)
#     result.append(odd_total)
#     return result

# def count_odd_even_rows(sample_list):
#     result = []
#     odd_total = 0
#     even_total = 0
#     for row in sample_list:
#         total = sum(row)
#         if total % 2 == 0:
#             even_total += 1
#         elif total % 2:
#             odd_total += 1
#     result.append(even_total)
#     result.append(odd_total)
#     return result
#
# ################### Sample Solution ###################
# def _count_even_sum_sample_(sample_2d_list):
#     even_count = 0
#     odd_count = 0
#     # For each row
#     for rows in sample_2d_list:
#         row_sum = sum(rows)
#         if row_sum % 2 == 0:
#             even_count = even_count + 1
#         else:
#             odd_count = odd_count + 1
#     return [even_count, odd_count]
#
#
# my_list = [[90, 87, 95], [78, 91, 89],
#              [83, 85, 91]]
# print(count_odd_even_rows(my_list))


# Multidimensional Lists Exercise 7 (List of Row Maximums)

'''Write a function that takes a two-dimensional list
(list of lists) of numbers as argument and returns a list which
 includes the maximum value of each row.
'''
# def list_of_row_max(sample_list):
#     max_vals = []
#     for rows in sample_list:
#         max_val = None
#         for number in range(len(rows)):
#             if max_val == None or rows[number] > max_val:
#                 max_val = rows[number]
#         max_vals.append(max_val)
#     return max_vals

# def list_of_row_max(sample_list):
#     return [max(row) for row in sample_list]


# my_list = [[90, 87, 95], [78, 81, 89],
#              [83, 85, 91]]
# print(list_of_row_max(my_list))


# Multidimensional Lists Exercise 8 (List of Column Maximums)

'''Write a function that takes a two-dimensional list
(list of lists) of numbers as argument and returns a list which
includes the maximum value of each column. Assume that the length
of columns is consistent in each row.
'''

# def _sum_of_columns_sample_(sample_list):
#     # Solution type 1:
#     # return [max(col) for col in zip(*sample_list)]
#     # Alternative Solution
#     cols = len(sample_list[0])
#     mylist = []
#     for c in range(cols):
#         # iterating over each column
#         column_sum = 0
#         for row in sample_list:
#             print(row[c])
#             column_sum += row[c]
#         mylist.append(column_sum)
#     return mylist
#

# def list_of_col_max(sample_list):
#     cols = len(sample_list[0])
#     max_cols = []
#     for c in range(cols):
#         max_col = None
#         for row in sample_list:
#             if max_col == None or row[c] > max_col:
#                 max_col = row[c]
#         max_cols.append(max_col)
#     return max_cols
#
# ################### Sample Solution ###################
# def _max_of_columns_sample_(sample_list):
#     cols = len(sample_list[0])
#     mylist = []
#     for c in range(cols):
#         column_max = 0
#         for row in sample_list:
#             if row[c] > column_max:
#                 column_max = row[c]
#         mylist.append(column_max)
#     return mylist


# my_list = [[90, 87, 95], [78, 81, 89],
#            [83, 85, 91]]
# print(list_of_col_max(my_list))


# Multidimensional Lists Exercise 9 (2D To 1D)

'''Write a function that accepts a 2-dimensional list of integers,
 and returns a sorted (ascending order) 1-Dimensional list
 containing all the integers from the original 2-dimensional list.
'''

# def sort_2d_list(sample_list):
#     one_d_list = [number for row in sample_list for number in row]
#     one_d_list.sort()
#     return one_d_list
#
# my_list = [[90, 87, 95], [78, 81, 89],
#            [83, 85, 91]]
# print(sort_2d_list(my_list))


# Multidimensional Lists Exercise 10 (Sort Rows)

'''Write a function that accepts a 2-dimensional list of integers,
 and sorts (descending order) all the elements inside each row and
  returns the sorted 2-dimensional list.
'''

# def sort_rows_reverse(sample_list):
#     sorted_list = []
#     for row in sample_list:
#         row = sorted(row, reverse = True)
#         sorted_list.append(row)
#     return sorted_list
#
# ################### Sample Solution ###################
# def _2d_rows_sorted_sample_(_2d_list):
#     for rows in _2d_list:
#         rows.sort(reverse=True)
#     return _2d_list


# my_list = [[90, 87, 95], [78, 81, 89],
#            [83, 85, 91]]
#
# print(sort_rows_reverse(my_list))



# Multidimensional Lists, Exercise 11 (Multiplication Check of two Matrices)

'''Write a function that accepts two (matrices) 2 dimensional
lists a and b of unknown lengths and returns True if they can be
multiplied together False otherwise. Hint: Two matrices a and b
can be multiplied together only if the number of columns of the
first matrix(a) is the same as the number of rows of the second
matrix(b). The input for this function will be two 2 Dimensional
lists. For example if the input lists are:

a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]

Then your function should return a boolean value:

True
'''

# def mult_check_2_matrices(sample_a, sample_b):
#     col_length = len(sample_a[0])
#     row_count = 0
#     for row in sample_b:
#         row_count += 1
#     if row_count == col_length:
#         return True
#     return False
#
# ################### Sample Solution ###################
# def _multiplication_check_sample_(a, b):
#     columns_of_a = len(a[0])
#     rows_of_b = len(b)
#     if columns_of_a == rows_of_b:
#         return True
#     else:
#         return False


# a = [[2, 3, 4],
#      [3, 4, 5]]
#
# b = [[4, -3, 12],
#      [1, 1, 5],
#      [1, 3, 2]]
#
# print(mult_check_2_matrices(a, b))


# Multidimensional Lists, Exercise 12 (Multiplication of two Matrices)

'''Write a function that accepts two (matrices) 2 dimensional
lists a and b of unknown lengths and returns their product. Hint:
 Two matrices a and b can be multiplied together only if the number
  of columns of the first matrix(a) is the same as the number of
  rows of the second matrix(b). Hint: You may import and use the
  numpy module but your return must be a python list not a numpy
  array. The input for this function will be two 2 Dimensional
  lists. For example if the input lists are:

a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]

Then your function should return their product such as:

[[15, 9, 47], [21, 10, 66]]
'''


################### Sample Solution ###################
# def _product_of_two_vectors_sample_(a, b):
#     import numpy
#     product = (numpy.mat(a) * numpy.mat(b))     # returns a numpy array
#     product_to_list = product.tolist()          # convert the numpy array to a standard list
#     return product_to_list
#
#
# a = [[2, 3, 4],
#      [3, 4, 5]]
#
# b = [[4, -3, 12],
#      [1, 1, 5],
#      [1, 3, 2]]
#
# print(mult_check_2_matrices(a, b))



# Multidimensional Lists, Exercise 13 (Multiplication of two Matrices without numpy)

'''Write a function that accepts two (matrices) 2 dimensional
lists a and b of unknown lengths and returns their product. Hint:
Two matrices a and b can be multiplied together only if the number
 of columns of the first matrix(a) is the same as the number of
  rows of the second matrix(b). Do NOT use numpy module for this
  exercise. The input for this function will be two 2 Dimensional
  lists. For example if the input lists are:

a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]

Then your function should return their product such as:

[[15, 9, 47], [21, 10, 66]]

'''

################### Sample Solution ###################
def _product_of_two_vectors_sample_(a, b):
    if len(a[0]) != len(b):
        return None
    # Create the result matrix and fill it with zeros
    output_list=[]
    temp_row=len(b[0])*[0]
    for r in range(len(a)):
        output_list.append(temp_row[:])
    for row_index in range(len(a)):
        for col_index in range(len(b[0])):
            sum=0
            for k in range(len(a[0])):
                sum=sum+a[row_index][k]*b[k][col_index]
            output_list[row_index][col_index]=sum
    return output_list


a = [[2, 3, 4],
     [3, 4, 5]]

b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]
print(_product_of_two_vectors_sample_(a,b))