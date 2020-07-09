# This projects prompts user to enter numbers to find min and max. Prompt will ask
# to enter until user adds 999

SENTINEL = 999
haveAllData = False
numberCount = 0

while not haveAllData :
    value = float(input('Enter value '))
    if value == SENTINEL :
        haveAllData = True
    else:
        numberCount += 1
        if numberCount == 1  :
           maximum = value
           minimum = value
        else:
            if value > maximum :
               maximum = value
            if value < minimum :
               minimum = value

if numberCount == 0:
    print ('you entered no data')
else:
    print ('max is ', maximum)
    print ('min is ', minimum)
