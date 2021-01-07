print("""
##################################
least common multiple (Burak Ibrahim Unal)
##################################
""")
def findLeast(number1, number2):
    i = 2
    lcm = 1
    while True:
        if (number1 % i == 0 and number2 % i == 0):
            lcm *= i
            number1 /= i
            number2 /= i
        elif (number1 % i == 0 and number2 % i != 0):
            lcm *= i
            number1 /= i
        elif (number1 % i != 0 and number2 % i == 0):
            lcm *= i
            number2 /= i
        else:
            i += 1
        if (number1 == 1 and number2 == 1):
            break
    return lcm
number1 = int(input("Number-1:"))
number2 = int(input("Number-2:"))
print("Least common multiple:", findLeast(number1, number2))
