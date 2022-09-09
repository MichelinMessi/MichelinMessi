import math
def isPrime(n):
    if n==2 or n==3:
        return True
    if n%6!=1 and n%6!=5 or n<=1:
        return False
    for i in range(5,int(math.sqrt(n))+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True


n = int(input())
count = 0
for i in range(2,n-1):
    if isPrime(i):
        if isPrime(i+2):
            
            count += 1
print(count)
