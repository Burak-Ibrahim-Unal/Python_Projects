print("""
##################################
largest common divisor (Burak Ibrahim Unal)
##################################
""")

def findLargest(number1, number2):
    stack1 = {1}  # Aliquot stack that divide number1 which first element is 1...
    stack2 = {1}  # Aliquot stack that divide number2 which first element is 1...

    for i in range(2, number1 + 1):
        if number1 % i == 0: 
            stack1.add(i) 

    for j in range(2, number2 + 1):
        if number2 % j == 0:
            stack2.add(j)

    common_divisors = stack1 & stack2  # intersecting elements...
    largest_common_divisor = max(common_divisors)  # max number of intersecting elements...
    print("Largest common divisor of {} and {} numbers is = {}.".format(number1, number2 , largest_common_divisor))
    return largest_common_divisor


while True:
    number1 = int(input("Please enter first number for largest common divisor:"))
    number2 = int(input("Please enter second number for largest common divisor:"))
    findLargest(number1, number2)

