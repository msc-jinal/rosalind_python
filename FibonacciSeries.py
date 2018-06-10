import sys

def fibo(total):
    n1=0
    n2=1
    if(total<=1):
        return 0
    str=[n1,n2]
    for i in range(2,total):
        n3 = n1+n2
        n1=n2
        n2=n3
        str.append(n3)
    return str



def fib(x):
    l=[]
    for i in range(0,x):
        if len(l) < 2:
            l.append(i)
        else:
            l.append(l[i-2]+l[i-1])

    return l;



print('User Input: ',sys.argv[1])
l2=fib(int(sys.argv[1]))
print(l2)

