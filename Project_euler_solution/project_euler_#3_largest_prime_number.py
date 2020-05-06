import sys


t = int(input().strip())
for a0 in range(t):
    rslt=0
    n = int(input().strip())
    while n%2==0:
        n=n/2
        rslt=2
    for i in range(3,int(n**0.5)+1,2):
        while n%i==0:
            n=n/i
            rslt=i
    if n>2:
        rslt=int(n)
    print(rslt)
