n = eval(input())
n_list=[]
for i in range(n):
    na = input().split()
    n_list.append(na)

for j in range(len(n_list)):
    a, b ,c = map(int,n_list[j])
    if a + b > c:
        print('Case #{}: true'.format(j+1))
    else:
        print('Case #{}: false'.format(j+1))