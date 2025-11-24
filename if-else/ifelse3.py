'''Write a Python program that asks the user for three numbers.
Your program should print:

The largest number

The smallest number

And also check if all three numbers are equal

And if they are not equal, print whether

They form an increasing sequence (ex: 2, 7, 10)

They form a decreasing sequence (ex: 10, 7, 1)

Or no particular sequence'''

a=int(input("Enter the first number"))
b=int(input("ENter the second number"))
c=int(input("ENter the third number"))

#checking for same number 
if (a==b==c):
    print("all numbers are the same ")
    
#if a is bigger 
elif (a>b and a>c):
    print("the largest is ",a)
    #finding the smallest
    if (b<c):
        print("the smallest is ",b)
    else:
        print("the smallest is ",c)
#if b is bigger
elif (b>a and b>c ):
    print("the largest is ",b)
    #finding the smallest
    if (a<c):
        print("the smallest is ",a)
    else:
        print("the smallest is ",c)
#if c is bigger
elif (c>a and c>b):
    print("the largest is ",c)
    #finding the smallest
    if (b<a):
        print("the smallest is ",b)
    else:
        print("the smallest is ",a)
else:
    print("Enter valid number")
    print("no particualr sequence ")

#finding sequence 
if a < b < c:
    print("Increasing sequence")
elif a > b > c:
    print("Decreasing sequence")
else:
    print("No particular sequence")
