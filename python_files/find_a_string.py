def count_substring(string, sub_string):
    countt=0
    temp1=0
    for i in range(len(string)):
        if(string[i]==sub_string[0]):
            temp=1
            temp1=i+1
            for j in range(1,len(sub_string)):
                if (temp1<len(string) and string[temp1]==sub_string[j]):
                    temp=temp+1
                    temp1=temp1+1
                else:
                    break
            
            if(temp==len(sub_string)):
                countt=countt+1
    
            i=temp        
                                
    return countt

if __name__ == '__main__':