n = list(map(int,input().split(' ')))
len_n = n[0]
nl=n[1:]
A1,A2,A3,A4,A5=0,0,0,0,0
#交叉指示位
flag=0
n4=0
max_n=0
for i in range(len_n):
    if nl[i] % 10 ==0:
        A1 += nl[i]

    elif nl[i] % 5 == 1:
        A2 += nl[i] * (-1) ** flag
        flag += 1

    elif nl[i] % 5 == 2:
        A3+= 1

    elif nl[i] % 5 == 3:
            n4 += 1
            A4 += nl[i]

    elif nl[i] % 5 == 4:
        if nl[i] > A5:
            A5 = nl[i]

if A1==0:
    A1='N'
if A2==0:
    A2='N'
if A3==0:
    A3='N'
if A4==0:
    A4='N'
else:
    A4=round((A4/n4),1)
if A5==0:
    A5='N'

print(A1,A2,A3,A4,A5)

