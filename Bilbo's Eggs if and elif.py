# This program uses if and elif to calculate complex purchasing decision
#Bilbo's Eggs

number_of_eggs = int (input('Enter the number of eggs: '))

#Calculate price per egg:

if number_of_eggs < 12*4:
    Price=0.5
elif number_of_eggs >=12*4 and number_of_eggs < 12*6:
    Price=0.45
elif  number_of_eggs >= 12*6 and number_of_eggs < 12*11:
    Price=0.4
else:
    number_of_eggs >= 12*11
    Price=0.35

Total_bill= number_of_eggs * Price/12

print ('Your cost is', Price , 'per dozen, or', Price/12, 'per egg')
print ('Your bill comes to' , Total_bill)

    
