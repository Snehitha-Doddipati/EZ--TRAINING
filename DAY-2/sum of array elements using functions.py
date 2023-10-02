'''sum of array elements using functions?'''
#declaring function
def sum_array(array):
  total = 0
  for element in array:
    total += element
  return total

# taking input from user
array = list(map(int,input("enter array elements :").split(" ")))
sum = sum_array(array)
print("sum is :",sum)