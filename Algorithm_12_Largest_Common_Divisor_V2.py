print("""
##################################
largest common divisor v2(Burak Ibrahim Unal)
##################################
""")

def findLargest(number1, number2):

    i = 1
    lcd = 1
    while (i <= number1 and i <= number2):

        if (not (number1 % i) and not (number2 % i)):
            lcd = i
        i += 1
    return lcd
number1 = int(input("Number1:"))
number2 = int(input("Number2:"))

print("Largest common divisor is:", findLargest(number1, number2))
