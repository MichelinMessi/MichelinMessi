import math

# 函数用来判断是否为素数
def isprime(n):
    # n为2或3，可以直接判断是素数
    if n == 2 or n == 3:
        return True
    # n可以被2或3整除，可以直接判断不是素数
    if n % 2 == 0 or n % 3 == 0:
        return False
    '''
    11 13 17 19 23 29 31 37 41 43
47 53 59 61 67 71 73 79 83 89
97 101 103
可以观察到除了2，3，其余素数都分布在6n（n>=1）左右
    '''
    for k in range(6, int(math.sqrt(n)) + 2, 6):
        if n % (k - 1) == 0 or n % (k + 1) == 0:
            return False
    return True
m,n = list(map(int,input().split()))
#第几个素数
p = 0
#从1开始
i = 1
#10个数字一行
ten=1

while p < n:
    i += 1
    if isprime(i):
        p += 1
        if p >= m:
            #如果满一行，或者是最后一个输出
            if ten == 10 or p == n:
                print(i)
                ten = 1
            else:
                print(i,end=' ')
                ten += 1
