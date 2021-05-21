#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s1=""
    i=0
    while(i<len(s)):
        #print(i)
        if(i==0):
            s1=s1+s[i].upper()    
        elif(s[i-1]==' '):
            s1=s1+s[i].upper()
            #print(s1)
        else:
            s1=s1+s[i]  
        i+=1    
    #print(s1)
    return s1       
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
