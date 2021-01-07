

def main():
    mylist = [34,-93,10,-9,13,22,1,88,-178,45]
    removeMin(mylist)
    print("My new list is:{} and \n multiply result of my array between minimum and maximum number is {}".format(mylist,multipl(mylist)))

def removeMin(list):
    list.sort()
    list.pop(0)
    return list

def multipl(list):
    result=1
    for i in range(len(list)):
        if list[i]==min(list) or list[i]==max(list):
            continue
        else:
            result *= list[i]
    return  result

main()