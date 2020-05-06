import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    rslt=2
    a=1
    b=2
    i=0
    if n==1:
        print(0)
    elif n==2:
        print(2)
    while(i<n):
        c=a+b
        a=b
        b=c
        if c<n and c%2==0:
            rslt+=c
        elif c>n:
            break
        
        i=i+1
    print(rslt)