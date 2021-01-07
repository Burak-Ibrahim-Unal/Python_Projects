def createList():
    numList=[]
    print("Enter numbers and type q for calculating:")
    while True:
        x=input()
        if (not x.isnumeric() and x=="q"):
            break
        numList.append(int(x))
    return numList

###print(createList())
###print(sumList(createList()))

def sumList(lst):
    sum=0
    for i in range(len(lst)):
        sum+=lst[i]
    """for i in lst:
        sum+=i"""
    return sum

def avgList(lst):
    sum=0
    for i in range(len(lst)):
        sum+=lst[i]
    avg=sum/len(lst)
    return avg

def compareList(lst):
    """newList=[]
    for i in range (len(lst)):
        if (lst[i]>avgList(lst)):
            newList.append(lst[i])
    return newList"""
    sum=0
    for i in range(len(lst)):
        if (lst[i] > avgList(lst)):
            sum+=lst[i]
    return sum

def minValue(lst):
    min_location=0
    for i in range (len(lst)):
        if (min(lst)==lst[i]):
            min_location=i
    return min(lst),min_location

def maxValue(lst):
    max_location=0
    for i in range (len(lst)):
        if (max(lst)==lst[i]):
            max_location=i
    return max(lst),max_location

def maxValue2(lst):
    return max(lst),lst.index(max(lst))

def minValue2(lst):
    return min(lst),lst.index(min(lst))


def main():
    L=createList()
    print("Sum=",sumList(L))
    print("Avg=",avgList(L))
    print("Sum of Bigger than Avg=",compareList(L))
    m1,p1=minValue(L)
    m2,p2=maxValue(L)
    print("Min Value=" + m1 + " Min location=" + p1 +" Max Value=" + m2 +" and max location="+p2)

main()