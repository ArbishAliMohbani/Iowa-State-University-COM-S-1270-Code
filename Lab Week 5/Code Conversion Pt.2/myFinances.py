def annualPercentageRate(interest_charges1, fees1, loan_amount1, days_in_term1):
    apr = (((interest_charges1 + fees1) / loan_amount1) / days_in_term1) * 100
    return apr

def compoundAmount(principal1, rate1, number_compounds1, time1):
    accured_amount = principal1 * (1 + (rate1/100) / number_compounds1) ** (number_compounds1 * time1)
    return accured_amount