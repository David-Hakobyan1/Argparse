import argparse

def fib(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a

def gumarum(a,b):
    return a+b

def main():
    parser = argparse.ArgumentParser()
    parser1 = argparse.ArgumentParser()
    parser.add_argument("num",help="The fibonacci number you wish to calculate.",type=int)
    parser1.add_argument("n1","n2",help="gumarman tver",type=int)
    args1 = parser1.parse_args()
    args = parser.parse_args()
    result = fib(args.num)
    result1 = gumarum(args1.n1,n2)
    print("the " + str(args.num) + "th fib numbers is " + str(result))
    print("gumar@ " +(args1.n1,n2) + " havasar e " + str(result1))

if __name__=="__main__":
    main()


