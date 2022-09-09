'''
#中文注释的问题？
搞不懂，非零返回问题经常出现
'''
s1 = list(input())
s2 = list(input())
s3 = list(input())
s4 = list(input())

day = {'A': 'MON', 'B': 'TUE', 'C': 'WED', 'D': 'THU', 'E': 'FRI', 'F': 'SAT', 'G': 'SUN'}
flag = False
for i in range(min(len(s1), len(s2))):

    if ('A' <= s1[i] <= 'G') and (s1[i] == s2[i]) and (not flag):
        print(day.get(s1[i]), end=' ')
        flag = True

    elif s1[i] == s2[i] and flag:
        if 'A' <= s1[i] <= 'N':
            print((ord(s1[i]) - ord('A') + 10), end=':')
            break
        elif '0' <= s1[i] <= '9':
            print('{:02}'.format(ord(s1[i])-ord('0')), end=':')
            break
for i in range(min(len(s3), len(s4))):
    if ('a' <= s3[i] <= 'z' or 'A' <= s3[i] <= 'Z') and (s3[i] == s4[i]):
        print('{:02}'.format(i))
        break
