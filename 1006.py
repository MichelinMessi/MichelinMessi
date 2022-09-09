'''
简单的分类
'''
n = int(input())

hun = int(n / 100)
ten = int((n % 100)/10)
single = (n % 10)
r_single = ""

for i in range(1,single+1):
    r_single +=str(i)

result = 'B'*hun + 'S'*ten + r_single

print(result)

