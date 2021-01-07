def main():
    while(True):
        cardnumber=input("Please enter 16 digit credit card number or press q button to exit...\n")
        if(cardnumber=="q"):
            break
        else:
            SumNo(cardnumber)

def SumNo(number):
    sum1=sum2=0
    for i in range(0,len(number)):
        if i%2==0:
            sum1 += (int(number[i])*2 % 10)+1
        else:
            sum2 += int(number[i])
    if(sum1+sum2) % 10 == 0:
        print("Credit card is valid")
    else:
        print("Credit card is not valid")

main()