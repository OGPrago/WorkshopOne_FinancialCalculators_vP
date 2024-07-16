from Calculators import mortgageCalc, cdCalc, presentValueCalc

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