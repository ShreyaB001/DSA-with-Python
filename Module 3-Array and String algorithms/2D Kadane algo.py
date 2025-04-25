def matrix(arr):
    if not arr or not arr[0]:
        return 0
    rows=len(arr)
    cols=len(arr[0])
    max_sum=float('-inf')
    for top in range(rows):
        temp=[0]*cols
        for bottom in range(top,rows):
            for col in range(cols):
                temp[col]+=arr[bottom][col]
            curr_sum=temp[0]
            best_sum=temp[0]
            for i in range(1,cols):
                curr_sum=max(temp[i],curr_sum+temp[i])
                best_sum=max(curr_sum,best_sum)
            max_sum=max(best_sum,max_sum)
    return max_sum

arr= [
    [1, 2, -1],
    [-3, 4, 5],
    [2, -6, 3]
]
print(matrix(arr))