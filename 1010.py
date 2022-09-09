#存入列表中，开导
bin = list(map(int,input().split()))#用split(' ')会有非零返回错误
#解答：split()的时候，多个空格当成一个空格；split(' ')的时候，多个空格都要分割，每个空格分割出来空。
lbin = len(bin)
cbin = []

for i in range(0,lbin,2):
        #系数
        xs = bin[i] * bin[i+1]
        #指数
        zs = bin[i+1] - 1
        #如果求导后系数为0，则跳过
        if xs:
            cbin.append(str(xs))
            cbin.append(str(zs))

if len(cbin):
    print((' ').join(cbin))
else:
    print('0 0')