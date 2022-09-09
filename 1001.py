#简单的累加
n = int(input())
flag=0
while(n!=1):
    if(n%2==0):
        n/=2
    else:
        n=3*n+1
        n/=2
    flag+=1

print(flag)