#In the given array every  number occurs twice only 1 no occues 1 time?
def find_single(arr,n):
    res = arr[0]
    for i in range (1,n):
        res = res ^arr[i]
    return res
arr = [2,3,5,4,5,3,4,2,88]
print(find_single(arr,len(arr)))
