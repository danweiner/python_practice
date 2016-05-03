# Part 1: Calculate monthly payments for a loan

'''Write a function that calculates and returns the monthly payments
for a loan. This function accepts three parameters in the exact order
(principal, annual_interest_rate, duration)
'''

##def calc_monthly_payments(principal, annual_interest_rate, duration):
##    r = (annual_interest_rate / 100) / 12
##    n = duration * 12
##    if r == 0 :
##        monthly_payment = (principal / n)
##    else:
##        monthly_payment = (principal) * (r * (1+r)**n) / ((float(1+r)**n) - 1)
##    return monthly_payment
##
##print(calc_monthly_payments(1000.0, 4.5, 5))
##
##################### Sample Solution ###################
##def _calculate_payment(principle, interest_rate_per_year, duration):
##    if interest_rate_per_year==0:
##        return principle/(duration*12)
##    r=interest_rate_per_year/100/12
##    n=duration*12
##    montly_payment=principle*(r*((1.0+r)**n))/(float((1.0+r)**n)-1.0)
##    return montly_payment


# Part 2: Calculate the remaining balance of a loan

'''Write a function that calculates and returns the remaining loan balance.
This function accepts four parameters in the exact order shown below:
(principal, annual_interest_rate, duration , number_of_payments)
'''
##def calc_remaining_balance(principal, annual_interest_rate, duration, number_of_payments):
##    r = (annual_interest_rate / 100) / 12
##    print('r is', r)
##    n = duration * 12
##    print('n is', n)
##    p = number_of_payments
##    print('p is', p)
##    if r == 0 :
##        remaining_balance = (principal) * ( 1 - ( p/n))
##    else:
##        remaining_balance = principal * ((1+r)**n - (1 + r)**p) / ((float(1+r)**n) - 1)
##    return remaining_balance
##
##print(calc_remaining_balance(1000.0, 4.5, 5, 12))
##
##################### Instructor function ###################
##def _calculate_balance(principal, interest_rate_per_year, duration, number_of_payments):
##    if interest_rate_per_year==0:
##        return principal-number_of_payments*(principal/(duration*12.0) )   
##    r=interest_rate_per_year/100/12.0
##    n=duration*12
##    balance=principal*((1.0+r)**n - (1.0+r)**number_of_payments) / (((1.0+r)**n)-1)
##    return balance


# Part 3: Display loan information

'''Write a program for loan calculations. Your program should ask the user for
three pieces of information (with three seperate input() functions:)
 - Total amount of loan.
 - Annual interest rate. (Assume that the interest rate is a positive integer. For example 5 means that annual interest is 5% (five percent) per year.
 - Total duration of loan in years.
Your Program should use the two functions that you implented in part 1 and 2
of this exercise and display the follwoing information about the loan.
 - In the first line show the amount of loan and interest rate.
 - In the second line show duration of the loan and monthly payment.
 - In each of the following lines show the Loan balance and total amount paid for each year.
'''



def calc_monthly_payments(principal, annual_interest_rate, duration):
    r = (annual_interest_rate / 100) / 12
    n = duration * 12
    if r == 0 :
        monthly_payment = (principal / n)
    else:
        monthly_payment = (principal) * (r * (1+r)**n) / ((float(1+r)**n) - 1)
    return monthly_payment

def calc_remaining_balance(principal, annual_interest_rate, duration, number_of_payments):
    r = (annual_interest_rate / 100) / 12
    n = duration * 12
    p = number_of_payments
    if r == 0 :
        remaining_balance = (principal) * ( 1 - ( p/n))
    else:
        remaining_balance = principal * ((1+r)**n - (1 + r)**p) / ((float(1+r)**n) - 1)
    return remaining_balance

def display_loan_info():
    principal = float(input("Enter loan amount: "))
    annual_interest_rate = float(input("Enter annual interest rate (percent): "))
    duration = int(input("Enter loan duration in years: "))

    monthly_payment = calc_monthly_payments(principal, annual_interest_rate, duration)
    print('LOAN AMOUNT:', principal, 'INTEREST RATE (PERCENT):', annual_interest_rate)
    print('DURATION (YEARS):', duration, 'MONTHLY PAYMENT:', int(monthly_payment))

    for year_number in range(1, duration + 1):
        y = calc_remaining_balance(principal, annual_interest_rate, duration, year_number*12)
        print('YEAR:', year_number, 'BALANCE:', int(y), 'TOTAL PAYMENT', int(monthly_payment * year_number * 12))

display_loan_info()
