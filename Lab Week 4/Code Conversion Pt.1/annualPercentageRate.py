# Arbish Ali Mohbani                    02/12/2025
# Lab # 3 

def annualPercentageRate(interest_charges1, fees1, loan_amount1, days_in_term1):
    apr = (((interest_charges1 + fees1) / loan_amount1) / days_in_term1) * 100
    return apr

def main():
    interest_charges = float(input("Enter the interest charges: "))
    fees = float(input("Enter the fees: "))
    loan_amount = float(input("Enter the loan amount: "))
    days_in_term = int(input("Enter the days in term: "))
    num1 = annualPercentageRate(interest_charges, fees, loan_amount, days_in_term)
    print("The Annual Percentage Rate is: "+str(num1))

if __name__ == "__main__":
    main()

# End
