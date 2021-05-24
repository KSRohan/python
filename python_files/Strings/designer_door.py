# Enter your code here. Read input from STDIN. Print output to STDOUT
a=input()
A=a.split(" ")
x1=int(A[0])
x2=int(A[1])

for i in range(x1//2):
    print(("-"*((x2-(6*i)-3)//2))+(".|."*(1+(2*i)))+("-"*((x2-(6*i)-3)//2)))

print(("-"*((x2-7)//2))+("WELCOME")+("-"*((x2-7)//2)))

for i in reversed(range(x1//2)):
    print(("-"*((x2-(6*i)-3)//2))+(".|."*(1+(2*i)))+("-"*((x2-(6*i)-3)//2)))
