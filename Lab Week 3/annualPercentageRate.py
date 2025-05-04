# Arbish Ali Mohbani                    02/11/2025
# Lab # 3 

interest_charges = float(input("Enter the interest charges: "))
fees = float(input("Enter the fees: "))
loan_amount = float(input("Enter the loan amount: "))
days_in_term = int(input("Enter the days in term: "))
apr = (((interest_charges + fees) / loan_amount) / days_in_term) * 100
print("The Annual Percentage Rate is: "+str(apr))

# End
