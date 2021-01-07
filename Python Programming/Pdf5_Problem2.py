def fac(n):
    multino = 1
    for i in range(1, n+1):
        multino *= i
    return multino

def e(n):
    sum = 1
    for i in range(1, n+1):
        sum += 1/fac(n)
    return sum

def main():
    for i in range(1, 21):
        print("e value={}".format(round(e(i), 2)))

main()

