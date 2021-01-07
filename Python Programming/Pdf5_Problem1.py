import math

def pi(n):
    p=0.0
    for i in range(1,n+1):
        x=1/(2*i-1)
        if i%2!=0:
            p+=x
        else:
            p+=-x
    return 4*p

def main():
    print("\u03C0={}".format(pi(1)))
    print("\u03C0={}".format(pi(1000)))
    print("\u03C0={}".format(pi(100000)))
    print("\u03C0={}".format(pi(1)))
    print("\u03C0={}".format(math.pi))


main()