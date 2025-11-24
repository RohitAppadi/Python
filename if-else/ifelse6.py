'''Write a Python program that checks if a person is eligible for a loan.
The program should ask for:
Age
Monthly income
Credit score
Existing loans count
Employment type
(accept only "salaried" or "self-employed")

➤ Loan Approval Rules:
✔ 1. Basic requirements

Age must be between 21 and 60

Monthly income must be >= 25,000

Credit score must be >= 650
Loan rejected: Basic requirements not met

'''
print("Welcome to our bank\nFor the loan approval fill out the neccesary details to check for eligibility")
age=int(input("Enter your age "))
monthly_income=int(input("Enter your monthly income "))
credit_score=int(input("Enter your credit score out of 1000 "))
existing_loans=int(input("Enter number of existing loans (0 if none) "))
employment_type=input("choose the employement type\nsalaried\nself-employed\n")

#Basic Requirement Checking
if ((21<=age<=60) and (monthly_income>= 25000) and (credit_score>= 650)):
    
    if (employment_type=="salaried" and credit_score>= 700 and existing_loans<= 2 ):
        print("Loan Approved")
    elif (employment_type=="self-employed" and credit_score>= 720 and existing_loans<= 1 and monthly_income>= 50000):
        print("Loan Approved")
    else:
         print("Loan rejected: Employment criteria not met")
        
else:
    print("Loan rejected: Basic requirements not met")
