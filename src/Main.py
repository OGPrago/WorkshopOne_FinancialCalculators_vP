import math

def main():
    print("Which calculator would you like to use?")
    print("\t1) Mortgage")
    print("\t2) Future Value")
    print("\t3) Present Value")
    userIn = int(input())

    if userIn == 1:
        principle = float(input("Enter the Principle: "))
        interestRate = float(input("Enter Interest Rate: "))
        loanTerm = int(input("Enter Loan length (in years): "))
        monthlyMortgage = mortgageCalc(principle, interestRate, loanTerm)
        totaledInterest = ((loanTerm * 12 * monthlyMortgage) - principle)
        print(f"A ${principle} loan at {interestRate}% interest for {loanTerm} years would have a ${monthlyMortgage}/mo payment with total interest of ${totaledInterest}")
    

    elif userIn == 2:
        deposit = float(input("Enter deposit amount: "))
        interestRate = float(input("Enter interest rate: "))
        years = int(input("Enter number of years: "))
        endingBal = cdCalc(deposit, interestRate, years)
        balanceDifference = endingBal - deposit
        print(f"If you deposit ${deposit} in a CD that earns {interestRate}% interest rate and matures in {years} years, your CD's ending balance will be ${endingBal} and you would have earned ${balanceDifference} in interest")

    elif userIn == 3:
        monthlyPayout = float(input("Enter the monthly payout: "))
        interestRate = float(input("Enter the expected interest rate: "))
        years = int(input("Enter number of years to payout: "))
        annuity = presentValueCalc(monthlyPayout, interestRate, years)
        print(f"To fund an annuity that pays ${monthlyPayout} monthly for {years} years and earns an expected {interestRate}% interest, you would need to invest ${annuity} today.")

    else:
        print("Wrong command.")

if __name__ == "__main__":
    main()        

    
def mortgageCalc(loan, rate, term):
    decimalInRate = float(rate / 100)
    mortgage = float(loan * (decimalInRate / 12) * (math.pow(1 + (decimalInRate / 12), 12 * term) / (math.pow(1 + (decimalInRate /12), 12 * term) - 1)))
    return mortgage

def cdCalc(deposit, rate, years):
    rate_decimal = rate / 100
    ending_bal = deposit * math.pow(1 + rate_decimal / 365, 365 * years)
    return ending_bal

def presentValueCalc(monthlyPay, intRate, years):
    decimalIntRate = intRate / 100
    periodIntRate = decimalIntRate / 12
    totalNumPeriods = years * 12
    presentValue = monthlyPay * ((1 - (math.pow(1 + periodIntRate, -totalNumPeriods))) / periodIntRate)
    return presentValue

    