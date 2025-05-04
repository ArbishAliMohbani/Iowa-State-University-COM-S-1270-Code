def studentLoanAmortization(period, payment_due, rate):
    monthly_rate = rate/12/100
    period_months = period*12
    monthly_payment = float((payment_due)*(((monthly_rate)*((1+monthly_rate)**period_months))/(((1+monthly_rate)**period_months)-1)))
    print("\nPeriod\tTotal Payment Due\tComputed Interest Due\tPrincipal Due\t\tPrincipal Balance")
    print("\t\t\t\t\t\t\t\t\t\t$"+str(payment_due)+"\n")
    principal_balance = payment_due
    computed_interest = principal_balance*monthly_rate
    principal_due = monthly_payment-computed_interest
    for i in range(1, period_months+1):
        principal_balance = principal_balance-principal_due
        print(str(i)+"\t$"+str(round(monthly_payment, 2))+"\t\t\t$"+str(round(computed_interest, 2))+"\t\t\t$"+str(round(principal_due, 2))+"\t\t\t$"+str(round(principal_balance, 2)))
        computed_interest = principal_balance*monthly_rate
        principal_due = monthly_payment-computed_interest

def main():
    period = int(input("Enter your Payment Period: "))
    payment_due = int(input("Enter your total Payment: "))
    rate = int(input("Enter the Interest Rate: "))
    studentLoanAmortization(period, payment_due, rate)

if __name__ == "__main__":
    main()