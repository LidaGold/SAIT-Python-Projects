# This program calcutlates New account balance given constant interest rate and year of investment
# use while to create a loop
# incorporate formats to make output more understandable

principle = float(input('What is your principle amount invested?: '))
interestRate = float(input('What is the annual interest rate (%) :',))
yearsEntered = int(input('How many years will this be invested for?:'))

#Formula 
#balance = balance * (1+interestRate)

balance = principle
years = 0
print ("   Years    Balance ")

while years < yearsEntered:
    balance += balance * (interestRate*0.01)
    years += 1

    print("   {:2d}      ${:,.2f}".format(years, balance))






               
