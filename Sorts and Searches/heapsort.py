def heapify(a,n,i):
    large=i
    l=2*i+1
    r=2*i+2

    if(l<n and a[i]<a[l]):
        large=l
    if(r<n and a[large]<a[r]):
        large=r

    if(large!=i):
        a[i],a[large]=a[large],a[i]

        heapify(a,n,large)

def heapsort(a):
    n=len(a)

    for i in range(n,-1,-1):
        heapify(a,n,i)

    for i in range(n-1,0,-1):
        a[i],a[0]=a[0],a[i]
        heapify(a,i,0)


a=[12,11,13,5,6,7]
heapsort(a)
print(*a,sep=' ')
