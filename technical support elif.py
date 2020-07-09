# This program allows user to enter Y/N to determine what is wrong with a computer
# The program is designed to apply if and elif concepts

 #design inputs 
computer_beep = input ('Does the computer beep when powered on? [Y/N] :')

computer_spin = input ('Does the drive spin when powered on? [Y/N] :')


#create if statements

if (computer_beep == 'Y') and (computer_spin =='Y'):
    print ('Contact Tech Support')
elif (computer_beep == 'Y') and (computer_spin =='N'):
    print ('Check drive cables')
elif (computer_beep == 'N') and (computer_spin =='N'):
    print('Bring computer to repair centre')
elif (computer_beep == 'N') and (computer_spin =='Y'):
    print ('Check the speaker contacts')
else: print("Do another test")



