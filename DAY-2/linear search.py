#linear search
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:#finding element in the array
            return i
    return -1

#taking input from user
arr = list(map(int,input("Enter array elements :").split(" ")))
x = int(input("enter element to search :"))
result = linear_search(arr, x)
print(f"Element found at index {result+1}")
