"""
PRINT LARGEST EVEN AND LARGEST ODD NUMBER IN A LIST
"""

n=int(input(" Enter the number of elements to be in a list:"))
b=[]
for i in range(0,n):
    a=int(input("element in a list:"))
    b.append(a)
c=[]
d=[]
for i in b:
    if(i%2==0):
        c.append(i)
    else:
        d.append(i)
c.sort()
d.sort()
count1=0
count2=0
for k in c:
    count1+=count1
for j in d:
    count2+=count2
print(" largest even number:",c[count1-1])
print("largest odd number:",d[count2-1])

          
OUTPUT-
Enter the number of elements to be in a list:5
element in a list:32
element in a list:56
element in a list:89
element in a list:98
element in a list:1
 largest even number: 98
largest odd number: 89
