import math_tools

a = int(input("Enter the first number:")) 

b = int(input("Enter the second number:")) 

operation = (input("Enter what operation you would like to perform:"))

if operation == "add":
    #print("operation was add")
    print(math_tools.add(a,b))
elif operation == "subtract":
    #print("operation was subtract")
    print(math_tools.subtract(a,b))
elif operation == "multiply":
    #print("operation was subtract")
    print(math_tools.multiply(a,b))
elif operation == "divide":
    #print("operation was subtract")
    print(math_tools.divide(a,b))

