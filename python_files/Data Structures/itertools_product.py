# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a=input()
b=input()

A = a.split(" ")
B = b.split(" ")

for i in range(len(A)):
    A[i]=int(A[i])
    
for i in range(len(B)):
    B[i]=int(B[i])

for i in range(len(list(product(A,B)))):
    print(list(product(A,B))[i],end=" ")
