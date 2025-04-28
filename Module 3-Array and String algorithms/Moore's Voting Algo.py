# MOORE'S VOTING ALGORITHM

def moore(arr):
    candidate=None
    count=0
    for num in arr:
        if count==0:
            candidate=num
        if num==candidate:
            count+=1
        else:
            count-=1
    if arr.count(candidate) > len(arr)//2:
        return candidate
    else:
        return -1

arr=[2,2,1,1,1,2,2]
print(moore(arr))