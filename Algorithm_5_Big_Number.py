print("Program that print highest number")

a=int(input("Please type first number:"))
b=int(input("Please type second number:"))
c=int(input("Please type third number:"))

if a>b and a>c:
    print("{} number bigger than {} and {}.".format(a,b,c))
elif b>a and b>c:
    print("{} number bigger than {} and {}.".format(b, a, c))
elif c>a and c>b:
    print("{} number bigger than {} and {}.".format(c, b, a))
