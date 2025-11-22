age = int(input("Enter your age: "))
if age < 10:
    print("you are not allowed to drive ")
elif 16<age<18:
    print("you can drive a 100 cc bike ")
elif age >= 18:
    print("you are elgible to drive any vehicle ")
else:
    print("Enter a valid age ")
    