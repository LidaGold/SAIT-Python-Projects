 # use while to create a loop to calculated investment
 # This program asks user to enter $ amount for priciple and add annual rate.
 # To stop the program user needs to entre SENTENIAL flag which is 0

SENTENIAL = 0 

years = 1

principle = float(input('What is your principle amount invested?: '))
interestRate = float(input('What is the interest rate year ' + str(years) +' in % :'))


balance=principle

while interestRate !=SENTENIAL:
      years+=1
      balance += balance*(interestRate *0.01)
      interestRate = float(input('What is the interest rate year ' + str(years) +' in % :'))
     
  
          
print ('At the end of', years, 'years your investment will be ${:,.2f}'.format(balance))
averageIncome = (balance -principle)/ (years -1)
print('Your average yearly income is ${:,.2f}'.format(averageIncome)) 


