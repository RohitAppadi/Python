'''Write a Python program that asks the user for two numbers and an operator
+   (addition)
-   (subtraction)
*   (multiplication)
/   (division)
%   (modulo)
'''

a = int(input("Enter the first number "))
b = int(input("Enter the second number "))

#taking operation 
print('''+. addition\n-. subtraction\n*. multiplication\n/. division\n%. modulo''')

op = input("Enter the corresponding sign to select you operation ")

# checking the operation 
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    if (b==0):
        print("cannot be divided by zero")
    else:
        print(a/b)
elif op=="%":
    if (b==0):
        print("cannot be divided by zero")
    else:
        print(a%b)
else:
    print("invalid operation")

    
    
    