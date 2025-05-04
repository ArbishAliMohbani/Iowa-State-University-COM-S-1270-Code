# Arbish Ali Mohbani                    02/11/2025
# Lab # 3 

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
number_compounds = float(input("Enter the times the interest compounds in a year: "))
time = int(input("How many times a year: "))
accured_amount = principal * (1 + (rate/100) / number_compounds) ** (number_compounds * time)
print("The Accured Amount is: "+str(accured_amount))

# End