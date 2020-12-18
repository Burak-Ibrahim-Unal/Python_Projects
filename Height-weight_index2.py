print("Height-weight index v2")

height=float(input("What is your height(cm):"))
weight=float(input("What is your weight(kg):"))
hwi=weight / (height**2)
if hwi < 18.5:
    print("You are weak...")
elif hwi < 25:
    print("Normal rate...")
elif hwi < 30:
    print("You must lose some weight...")
elif hwi > 30:
    print("Obese...")
else:
    print("Wrong values...")
