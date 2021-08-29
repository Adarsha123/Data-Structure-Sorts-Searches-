def interpolationSearch(a,n,x):
    lo=0
    hi=n-1
    while(lo<=hi and x>=a[lo] and x<=a[hi]):
        pos=lo+int(float((hi-lo)/(a[hi]-a[lo])*(x-a[lo])))
        if(a[pos]==x):
            return pos
        if(a[pos]<x):
            lo=pos+1
        if(a[pos]>x):
            hi=pos-1


    return -1

a=list(map(int,input().split()))
n=len(a)
x=int(input("Number you want to search: "))
pos=interpolationSearch(a,n,x)
if(pos!=-1):
        print("position is: ",pos)
else:
                
        print("Not found")
                
