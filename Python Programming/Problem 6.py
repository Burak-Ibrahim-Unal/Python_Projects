print("Height/Weight Program...")

boy=float(input("Height:"))
kilo=float(input("Weight:"))
bki=kilo / (boy**2)
if bki < 18.5:
    print("Underweight...")
elif bki < 25:
    print("Normal...")
elif bki >= 25:
    print("Overweight...")
else:
    print("Please write correct values...")