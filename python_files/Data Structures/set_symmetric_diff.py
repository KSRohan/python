# Enter your code here. Read input from STDIN. Print output to STDOUT

val1 = input()
val2 = input()
val3 = input()
val4 = input()

a1=set(val2.split(" "))
a2=set(val4.split(" "))

print(len(a1.symmetric_difference(a2)))
