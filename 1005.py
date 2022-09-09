#将过程产生的数存放在data列表中，然后将parm列表从大到小排序，如果一个数在parm
#中出现，但data中不存在，则可以确定这个数就是关键数，由于parm从大到小排序了，所以
#写进result列表中的数也是从大到小排序的
n = int(input())
parm = list(map(int,input().split()))#存放要计算的数
data = []
result = []
for temp in parm:
    while temp !=1:
        if temp%2 ==0:
            temp = int(temp/2)
            if temp not in data:
                data.append(temp)
        else:
            temp = 3*temp +1
            temp = int(temp/2)
            if temp not in data:
                data.append(temp)
parm.sort(reverse=True)
for i in parm:
    if i not in data:
        result.append(i)
i = 0
while i < len(result)-1:
    print(result[i],end=' ')
    i = i+1
print(result[i])
