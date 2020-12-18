print("""
#########################
Prime number with function...(Burak Ibrahim Unal)
#########################
""")
def prime_func(number1):
    if number1<=1:
        return False
    elif number1==2:
        return True
    else:
        for i in range(2,number1):
            if number1%i==0:
                return False
        return True
while True:
    number=input("Enter number please...")
    if number == "q":
            break
    else:
        number=int(number)
        if prime_func((number)):
            print("{} is prime number.".format((number)))
        else:
            print("{} is not prime number.".format(number))


