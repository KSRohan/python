if __name__ == '__main__':
    
    A=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        A.append([name,score])
    
    A.sort(key = lambda x: (x[1],x[0]))
    
    
    B=[]
    x=0
    
    for j in range(len(A)):
        if(A[j+1][1]>A[j][1]):
            x=A[j+1][1]
            break
    
    for k in range(len(A)):
        if(A[k][1]==x):
            print(A[k][0])