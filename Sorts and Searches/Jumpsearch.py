import math

def jumpsearch(a,n,key):
    m=int(math.sqrt(n))
    p=0
    while(a[min(m,n)-1]<key):
        p=m
        m+=m
        if(p>=n):
            return -1
    while(a[p]<key):
        p+=1
        if(p==min(m,n)):
            return -1
    if(a[p]==key):
        return p
    return -1

a=list(map(int,input().split()))
n=len(a)
key=int(input("Enter the key: "))
p=jumpsearch(a,n,key)
if(p>=0):
    print("found at ",p)
else:
    print("number not found ")
