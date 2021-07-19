import argparse

def gumarum(a,b):
    c = a+b
    return c

def Main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v","--verbose",action="store_true")
    group.add_argument("-q","--quiet",action="store_true")
    parser.add_argument("num",help="the fibonacci number you wish to calculate.",type=int)
    parser.add_argument("num1",help="the fibonacci number you wish to calculate.",type=int)
    parser.add_argument("-o","--output",help="output result to a file",action="store_true")
    args = parser.parse_args()
    result = gumarum(args.num,args.num1)
    if args.verbose:
        print("The " +str(args.num)+" + "+str(args.num1)+" = "+str(result))
    elif args.quiet:
        print(result)
    else:
        print("fib("+str(args.num)+") = "+str(result))

if __name__=="__main__":
    Main()
