#Author Lida Goldchteine
#The purpose of this program is to collect information from a user, calculate Gross Pay including
# overtime hours, and Net Pay and total amount of deductions based on user preference


#collect input data

employeeName = str(input('Please enter your full name: '))
numberOfHours = int(input('Please enter number of hours worked this week: '))
rateOfPay = float(input('Please enter your hourly rate $/h : '))

overTimeHours = numberOfHours - 40

# any number of hours greater than 40 is considered to be overtime
# user needs needs to be compensated for extra hours using using formula : hourly rate * 1.5


if numberOfHours<= 40:
        
    grossPay = numberOfHours*rateOfPay
    print (employeeName, 'your Gross Pay is: ${:,.2f}'.format (grossPay))
# determine overtime hours and calculate gross pay
else:
    grossPay = (40*rateOfPay) + overTimeHours*rateOfPay *1.5
    print(employeeName , 'your Gross Pay is : ${:,.2f},'.format (grossPay),'and number of overtime hours is:' ,overTimeHours)
   
    
# Calculate Net pay : Gross Pay  - Deductions

# If user decides to recieve Net Pay,  he/she needs to input the %ge to be deducted from his/her gross pay

deduction = str(input('Please indicate if you prefer deduction off your gross pay Y/N: '))           
if deduction == 'Y':
    deduction = float(input ('What % of gross pay to deduct? '))
    deductionAmount = grossPay*deduction*0.01
    NetPay = grossPay - deductionAmount
    print (employeeName, 'your deduction is : ${:,.2f},'.format(deductionAmount), 'and your Net Pay is :${:,.2f}'.format (NetPay))
else:
    print(employeeName, 'please consider adding deductions to help with taxes')

                       
                       
