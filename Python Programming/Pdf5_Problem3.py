import math

def mean_deviation(n):
    sum=0
    sum_x2=0
    print("Enter",n,"Numbers")
    for i in range(1,n+1):
        x=eval(input())
        sum+=n
        sum_x2+=x**2
    sum2=sum**2
    dev=math.sqrt((sum_x2-sum2/n)/(n-1))
    mean=sum/n
    return mean,dev

def main():
    n=eval(input("Enter numbers"))
    m,d=mean_deviation(n)
    print("Standart devitation:{}".format(round(d,2)))
    print("Mean:{}".format(m))

main()


