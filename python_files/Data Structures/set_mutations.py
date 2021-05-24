# Enter your code here. Read input from STDIN. Print output to STDOUT    `

m = input()
A = input()
n = input()

A1=set(A.split(" "))

for i in range(int(n)):
    n1 = input()
    B = input()
    B1 = set(B.split())
    
    if(n1[0]=='i'):
        A1.intersection_update(B1)
    elif(n1[0]=='u'):
        A1.update(B1)
    elif(n1[0]=='u'):
        A1.symmetric_difference_update(B1)
    else:
        A1.difference_update(B1)

        sum=0

for i in range(len(A1)):
    sum=sum+int(A1[i])
    
print(sum)    
    
            
            
            
       
