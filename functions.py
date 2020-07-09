def getValue(promt, minimum, maximum) :

    needValue=True
    while needValue:
        try:
            value= int(input('Enter value: '))
            if value < minimum or value > maximum :
                print ("entered value is outside of range", minimum, 'to', maximum)
            else:
                needValue = False
        except ValueError :
            print('Entered non -numeric value. Enter integers')

    return value

baselength= getValue('please enter base', 0,1000)
heightlength= getValue('please enter height',0,1000)
area= baselength * heightlength*0.5
print('area',  area)

