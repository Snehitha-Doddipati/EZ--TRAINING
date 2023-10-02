'''1.Implement 2d array and rotate the matrix in 90 degrees '''
# creating an 2d array
'''n=int(input("enter size of array:"))
martix=[]
for i in range(n):
    l=[]#this list is used for appending and refreshing into new row
    for j in range(n):
        l.append(input())
    martix.append(l)'''
matrix=[[1,2,3],[4,5,6,],[7,8,9]]
n=3
#printing orginal martix 
print('original matrix is :')
for row in matrix:
    print (*row)# '*' is using for removing list format

#transpose of martix
print("Transpose of Martix is : ")
for i in range(n):
    for j in (matrix):
        print(j[i], end= " ")
    print()

#rotate the matrix in 90 degrees
print("Rotate in 90 degrees is :")
for i in range(n):
    for j in range(n-1,-1,-1):
        print(matrix[i][j] ,end=" ") 
    print()