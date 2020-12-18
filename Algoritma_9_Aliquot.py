print("""
##############################
Aliquot 
##############################
""")
def findAliquot(number):
    divisor=[]

    for i in range(2,number):
        if number%i==0:
            divisor.append((i))
    return divisor

while True:
    number1=input("Please enter number or press q for exit...")
    if number1=="q":
        break
    else:
        number1=int(number1)
        print("Aliquots: {}".format(findAliquot(number1)))
