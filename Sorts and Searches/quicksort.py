def partition(a,low,high):
    i=low-1
    pivot=a[high]
    for j in range(low,high):
        if(a[j]<=pivot):
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[high]=a[high],a[i+1]
    return i

def quick(a,low,high):
    if(low<high):
        pi=partition(a,low,high)
        quick(a,low,pi)
        quick(a,pi+1,high)

a=[10,7,9,2,1]
n=len(a)
quick(a,0,n-1)
print(a)
        
    
    
