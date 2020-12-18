print("""
################################
Armstrong Number... (Burak Ibrahim Unal)
################################
""")
number1 = input("Please enter number:")
sum1 = 0
for i in range(len(number1)):
    sum1=sum1+(int(number1[i])**len(number1))
if sum1==int(number1):
    print("{} is Armstrong number.".format(number1))
else:
    print("{} is not Armstrong number.".format(number1))
