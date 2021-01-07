print("""
###############################
Factorial...(Burak Ibrahim Unal)
###############################
""")
while True:
    number1=int(input("Please enter number for Calculation:"))
    if number1 == "q":
        print("Program is closing...")
        break
    else:
        number1=int(number1)
        fac=1
        for i in range(1,number1+1):
            fac*=i
        print(fac)

