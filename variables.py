### get input from user using input([prompt])
### input returns a string even if user inputs a number
##user_response=input("Enter a temp in Celsius ")
### convert input to an int
##celsius = int(user_response)
##fahrenheit = ((celsius*9)/5)+32
##print(fahrenheit)

user_response = input("Please enter a radius value for a circle: ")
radius = int(user_response)
area = (radius * radius) * 3.14
perimeter = (radius * 2) * 3.14
print("The area is", area)
print("The perimeter is", perimeter)
