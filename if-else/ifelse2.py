'''WAP a python program Write a Python program that asks the user for a number and prints:

"Even and divisible by 5" if the number is even and divisible by 5

"Odd and divisible by 5" if the number is odd and divisible by 5

"Even but NOT divisible by 5" if it is even but not divisible by 5

"Odd but NOT divisible by 5" if it is odd but not divisible by 5'''

num=int(input("Enter the number to check "))

if (num%5==0 and num%2==0):
    print("number is divisible by 5 and is even!!")
elif (num%5==0 and num%2!=0):
    print("Number is divisible by 5 but is odd!!")
elif (num%5!=0 and num%2==0):
    print("number is even but not divisible by 5!!")
elif (num%5!=0 and num%2!=0):
    print("number is odd and not divisible by 5!!")
else:
    print("Enter a valid number")
    