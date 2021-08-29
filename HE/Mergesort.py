def mergesort(a):
    if(len(a)>1):
        mid=len(a)//2
        L=a[:mid]
        R=a[mid:]
        mergesort(L)
        mergesort(R)
        i=0
        j=0
        k=0
        while(i<len(L) and j<len(R)):
            if(L[i]<R[j]):
                a[k]=L[i]
                i+=1
            else:
                a[k]=R[j]
                j+=1
            k+=1
        while(i<len(L)):
            a[k]=L[i]
            i+=1
            k+=1
        while(j<len(R)):
            a[k]=R[j]
            j+=1
            k+=1
    
 


n=int(input())
a=list(map(int,input().split()))
print("before sorting : ",a)
mergesort(a)
print("After sorting: ",a)
