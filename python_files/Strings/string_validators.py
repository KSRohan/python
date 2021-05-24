if __name__ == '__main__':
    s = input()
    x=0
    A=["False","False","False","False","False"]
    for i in range(len(s)):
        if(s[i].isalnum()):
            A[0]="True"
    for i in range(len(s)):
        if(s[i].isalpha()):
            A[1]="True"
    for i in range(len(s)):
        if(s[i].isdigit()):
            A[2]="True"
            
    for i in range(len(s)):
        if(s[i].islower()):
            A[3]="True"
    for i in range(len(s)):
        if(s[i].isupper()):
            A[4]="True"                
    
            
    for i in range(len(A)):
        print(A[i])
            
        
