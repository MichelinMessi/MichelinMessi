'''
利用列表和元组做字典，记录每次输入的最大值最小值，再输出即可
'''
n = int(input())
stu_info={}
for i in range(1,n+1):
    name,number,grade = input().split()
    grade = int(grade)
    if i == 1:
        min = grade
        max = grade
    if grade < min:
        min = grade
    if grade > max:
        max = grade
    stu_info[grade]=(name,number)

print(stu_info.get(max)[0],stu_info.get(max)[1])
print(stu_info.get(min)[0],stu_info.get(min)[1])
