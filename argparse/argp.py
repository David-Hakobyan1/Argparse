# Argparse and fibonacci )))

import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

def fib(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a

def my_args():
    group.add_argument("-v","--verbose",action="store_true")
    group.add_argument("-q","--quiet",action="store_true")
    parser.add_argument("num",help="the fibonacci number you wish to calculate.",type=int)
    parser.add_argument("-o","--output",help="output result to a file",action="store_true")
    args = parser.parse_args()
    return args

def my_return(args,result):
    if args.output:
        print("result in file a fileris.txt")
        with open("fileris.txt","a") as f:
            f.write(str(result)+"\n")
    elif args.verbose:
        print("fib "+str(args.num)+" is "+str(result))
    elif args.quiet:
        print("fib("+str(args.num)+")="+str(result))
    else:
        print(result)

def main():
    args = my_args()
    result = fib(args.num)
    ret = my_return(args,result)

if __name__=="__main__":
    main()
