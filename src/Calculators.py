import math

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