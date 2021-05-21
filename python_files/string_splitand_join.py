def split_and_join(line):
    # write your code here
    
    A=line.split()
    a1=""
    for i in range(len(A)):
        if i==0:
            a1=a1+A[i]
        else:
            a1=a1+"-"
            a1=a1+A[i]    
        
    return a1
        
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)