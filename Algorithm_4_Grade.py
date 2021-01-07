print("""
##################################
Grade calculation (Burak Ibrahim Unal)
##################################
""")



exam1=int(input("Lütfen birinci vize notunu giriniz:"))
exam2=int(input("Lütfen ikinci vize notunu giriniz:"))
final=int(input("Lütfen final notunu giriniz:"))
grade= (exam1*30/100)+(exam2*30/100)+(final*40/100)

if grade>=90:
    print ("Your Grade is: AA")
elif grade >=85:
    print ("Your Grade is: BA")
elif grade >= 80:
    print("Your Grade is: BB")
elif grade>= 75:
    print("Your Grade is: CB")
elif grade >= 70:
    print("Your Grade is: CC")
elif grade >= 65:
    print("Your Grade is: DC")
elif grade >= 60:
    print ("Your Grade is: DD")
else:
    print("You failed to pas class...Study hard...")
