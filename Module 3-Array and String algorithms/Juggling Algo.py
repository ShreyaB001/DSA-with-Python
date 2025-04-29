# JUGGLING ALGORITHM

from math import gcd
def juggling(arr,d):
    n=len(arr)
    d=d%n
    g=gcd(d,n)
    for i in range(g):
        temp=arr[i]
        j=i
        while True:
            k=(j+d)%n  # this is for left rotation and for right rotation we use k=(j-d+n)%n
            if k==i:
                break
            arr[j]=arr[k]
            j=k
        arr[j]=temp
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
print(juggling(arr,2))
