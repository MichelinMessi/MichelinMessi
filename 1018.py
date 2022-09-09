import sys
n = int(input())
'''B,C,J'''
j = [0, 0, 0]
y = [0, 0, 0]
p = 0
for i in range(n):
    '''input().split()默认将每行最后的换行符删除，需要额外运算，所以有时候会出现运行超时'''
    a, b = sys.stdin.readline().split()
    if a == 'B' and b == 'C':
        j[0] += 1
    elif a == 'B' and b == 'J':
        y[2] += 1
    elif a == 'C' and b == 'J':
        j[1] += 1
    elif a == 'C' and b == 'B':
        y[0] += 1
    elif a == 'J' and b == 'B':
        j[2] += 1
    elif a == 'J' and b == 'C':
        y[1] += 1
    else:
        p += 1

print('{} {} {}'.format((j[0]+j[1]+j[2]), p, (y[0]+y[1]+y[2])))
print('{} {} {}'.format((y[0]+y[1]+y[2]), p, (j[0]+j[1]+j[2])))
if j[0] >= j[1] and j[0] >= j[2]:
    print('B', end=' ')
elif j[1] > j[0] and j[1] >= j[2]:
    print('C', end=' ')
else:
    print('J', end=' ')
if y[0] >= y[1] and y[0] >= y[2]:
    print('B')
elif y[1] > y[0] and y[1] >= y[2]:
    print('C')
else:
    print('J')
