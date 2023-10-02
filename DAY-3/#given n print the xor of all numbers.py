#given n print the xor of all numbers
n=int(input())
xor = 0
for i in range(n):
    xor = xor ^ i
print(xor)
