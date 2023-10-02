#After creating the array find out the smallest missing +ve integer
'''def solution(arr):
    positive_nums = [x for x in arr if x > 0]
    max_positive = max(positive_nums)
    positive_set = set(positive_nums)
    for i in range(1, max_positive ):
        if i not in positive_set:
            return i
arr=[3,1,-5,-6,0,4]
print(solution(arr))'''

'''arr = [3,1,-5,-6,0,4]
z=0
for i in arr:
    z= z+1
for i in range(0,z+1):
    if i in arr:
        continue
    else:
        break
print(i)'''

arr = [3,1,-5,-6,0,4]
pos = [i for i in arr if i > 0]
max_pos = arr[0]
for num in pos :
    if num > max_pos:
        max_pos = num
pos_set = set(pos)
for i in range (1,max_pos):
    if i not in  pos_set:
        print(i)