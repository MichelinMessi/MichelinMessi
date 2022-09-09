
'''
times = int(input())
check_ans = {}

for i in range(0,times):
    check_ans[i]=input()

def docheck(str):
    flag_p=0
    flag_t=0
    i=0
    flag_c=0
    len_str = len(str)
    str_b=''
    str_a=''
    if i < len_str:
        if str[i]!='P':

            if str[i]!=str[i+1]:
                a = i
                str_a = str[0:a]
                i+=1
        if str[i]=='P':
            flag_p +=1
            if flag_p>1:
                print('NO')
                return 0
            i += 1
        if str[i-1]=='P':
            if i != len_str:
                if str[i] != str[i+1]:
                    b = i
                    str_b = str[0:b-1]
            i += 1

        if str[i]=='T':
            flag_t += 1
            if flag_t > 1:
                print('NO')
                return 0
            i += 1
        if str[i-1]=='T':
            if i!=len_str:
                flag_c +=1
                i += 1
    if flag_c == len(str_a)*len(str_b):
        print('YES')
        return 1
for i in check_ans:
    docheck(check_ans[i])
'''
#利用正则表达式
import re
n = int(input())
for i in range(n):
    temp = input()
    if re.match(r'A*PA+TA*',temp):
        a = re.split(r'[P|T]',temp)#将字符串划分成三部分，即[XXX]P[AXXX]T[XXXX],满足第一部分与第二部分的长度乘积是第三部分的长度
        if a[0]*len(a[1]) == a[2]:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
