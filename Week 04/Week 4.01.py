Factors of a number
Determine the factors of a number (i.e., all positive integer values that evenly divide into a number).
For example:
Input
Result


20
1 2 4 5 10 20


k=int(input())
l=[]
for i in range(1,k+1):
    if(k%i==0):
        l.append(i)
for j in l:
    print(j,end=' ')
