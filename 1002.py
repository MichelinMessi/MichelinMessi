"""
利用字典将数字和拼音对应，计算输入和之后，str[i]找到对应拼音
"""
n = int(input())
result = {1:"yi",2:"er",3:"san",4:"si",5:"wu",6:"liu",7:"qi",8:"ba",9:"jiu",0:"ling"}
flag=0
if n < (10**100):
    str_n = str(n)
    for i in range(0,len(str_n)):
        flag = flag + int(str_n[i])

    str_flag = str(flag)
    for j in range(0,len(str_flag)):
        if j == len(str_flag)-1:
            print(result.get(int(str_flag[j])))
        else:
            print(result.get(int(str_flag[j])),end=" ")

'''
if(n<(10^100)):
    str_n = str(n)
    for i in range(0,len(str_n)):
        print(str_n[i])
    #for i in str_n:
        #print(str)
        #sum+=int(i)
    print(sum)
    sum = str(sum)
    for j in sum:
        print(result.get(j),end="")
'''
