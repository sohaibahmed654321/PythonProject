Name = input("Enter your name :" )
Salary = float(input("Enter your salary : "))
print("Expense Calculator : ")
grocerybill = float(input(":Enter your grocery bill : "))
KE_bill = float(input(":Enter your KE bill : "))
Gas_bill = float(input(":Enter your Gas bill : "))
Internet= float(input(":Enter your Internet : "))
Water_bill = float(input(":Enter your Water bill : "))
Jamedar = float(input(":Enter your Jamadar : "))
Supercard = float(input(":Enter your SuperCard : "))
Transport = float(input(":Enter your Transport : "))
Own_house = input("do You live In Own House :")

if Own_house.lower()=="no" :
    rent =float(input("Enter Your Rent :"))
else :
    rent = 0


Are_You_Married = input("Are You Married")
if Are_You_Married.lower() == "yes" :
    child =int(input("How many children do you have "))
    if child > 0 :
        child_expense = float(input("enter your child expense :"))
    else :
        child_expense = 0

Total_Expense = grocerybill + KE_bill + Gas_bill + Internet + Water_bill + Jamedar + Supercard + Transport + rent + child_expense
Saving =  Salary - Total_Expense

if Salary > Total_Expense :
    print(f"your Saving are : {Saving}.you should take saving plan kindly visit Meezan Bank.")
elif Salary == Total_Expense :
    print("Please You Should  Take Major Steps To Increase Income.")
else :
    print("Please Decraese Your Expenditure.")

print(f"Salary is :{Salary} .Total_Expense : {Total_Expense}")
print(f"Saving is : {Saving}")



