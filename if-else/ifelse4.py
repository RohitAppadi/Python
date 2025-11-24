'''Write a Python program to check a student's grade based on marks.

The program should:

Ask the user to enter marks out of 100.

Print the grade according to the following rules:
90–100  → Grade A
75–89   → Grade B
60–74   → Grade C
40–59   → Grade D
0–39    → Grade F
'''

marks = int(input("Enter the grade of the student "))
#checking for grade

if (90<=marks<=100):
    print("Grade A")
elif (75<=marks<=89):
    print("Grade B")
elif (60<=marks<=74):
    print("Grade C")
elif (40<=marks<=59):
    print("Grade D")
elif (0<=marks<=39):
    print("Grade F")
else :
    print("Invalid Marks")
    
    
    