#ask the user for three quiz marks
quiz1 = float (input("Enter quiz 1 mark: "))

quiz2 = float (input("Enter quiz 2 mark: "))

quiz3 = float (input("Enter quiz 3 mark: "))

#compute and output average
average = (quiz1 +quiz2+quiz3) / 3

print ('The average is', average)

# if Average is above 80 output special message
if average >= 85:
    print ('A')
else:
    if average >=70:
        print('B')
    else:
        if average >=60:
            print('C')
        else:
            if average >=56:
                print ('D')
            else:
                if average<56:
                    print ('F')
                else:
                    print('You are done')
