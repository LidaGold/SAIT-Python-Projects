# Calculate area of triangle using while not and if else
# Has UX component to 

goodBase = False
while not goodBase:
    base = int(input ('Enter the base :'))
    if base <= 0:
        print ('Error - the base length must be a positive number. You entered', base)
    else:
        goodBase = True


goodHeight = False
while not goodHeight:
    height = int(input ('Enter the height :'))
    if height <= 0:
        print ('Error - the height length must be a positive number. You entered', height)
    else:
        goodHeight = True

area = (base*height) / 2
print ('The area of the triangle: ', area)
