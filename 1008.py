'''
n,m = map(int,input().split(' '))
Alist=list(input().split(' '))

A = Alist[n-m:] + Alist[:n-m]
print(' '.join(A))
'''
n,m = map(int,input().split())
num1 = list(input().split())

num2 = []
for i in range(n):
    place = (i+m)%n
    num2.insert(place,num1[i])

print(' '.join(num2))
