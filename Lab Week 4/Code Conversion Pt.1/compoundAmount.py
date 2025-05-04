# Arbish Ali Mohbani                    02/12/2025
# Lab # 3 

def compoundAmount(principal1, rate1, number_compounds1, time1):
    accured_amount = principal1 * (1 + (rate1/100) / number_compounds1) ** (number_compounds1 * time1)
    return accured_amount

def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate: "))
    number_compounds = float(input("Enter the times the interest compounds in a year: "))
    time = int(input("How many times a year: "))
    num1 = compoundAmount(principal, rate, number_compounds, time)
    print("The Accured Amount is: "+str(num1))


if __name__ == "__main__":
    main()

# End