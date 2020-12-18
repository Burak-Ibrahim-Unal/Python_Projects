print("""
##############################
Perfect numbers between 1-1000... (Burak Ibrahim Unal)
##############################
""")

def perfect(number1):
    sum = 0
    for i in range(2,number1+1):
        if number1%i==0:
            sum+=number1/i
    if sum==number1:
        print("{} is perfect number...".format(number1))
    else:
        print("{} is not perfect number...".format(number1))
while  True:
    number=int(input("1-1000 arasında olmak üzere sayı giriniz:"))
    perfect(number)
