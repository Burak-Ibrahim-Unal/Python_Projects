"""
Leap Year (Burak Ibrahim Unal)

"""

while True:
    year=input("Please type year for checking leap year or press q button to exit\n")
    if year=="q":
        break
    else:
        intyear=int(year)
        if intyear%4==0 and intyear%100!=0 and intyear%4000!=0:
            print("Entered {} year is leap year".format(intyear))
        elif intyear%100==0 and intyear%400==0 and intyear % 4000!=0:
            print("Entered {} year is leap year".format(intyear))
        else:
            print("Entered {} year is not leap year".format(intyear))




