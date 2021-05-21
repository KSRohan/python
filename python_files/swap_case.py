def swap_case(s):
    a=""
    for i in range(len(s)):
        if s[i].islower():
            a=a+s[i].upper()
        elif s[i].isupper():
            a=a+s[i].lower()
        else:
            a=a+s[i]    
    
    return a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)