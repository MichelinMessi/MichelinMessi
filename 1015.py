'''两个超时'''
import sys
M, L, H = map(int, sys.stdin.readline().split())
stu = []
fir = []
sec = []
thi = []
fou = []
for i in range(M):
    stu.append(list(map(int, sys.stdin.readline().split())))

for j in range(M):
    if stu[j][1] >= H and stu[j][2] >= H:
        fir.append(stu[j])
    elif stu[j][1] >= H and L <= stu[j][2]:
        sec.append(stu[j])
    elif L <= stu[j][1] < H and L <= stu[j][2]:
        if stu[j][1] >= stu[j][2]:
            thi.append(stu[j])
        else:
            fou.append(stu[j])
print(len(fir)+len(sec)+len(thi)+len(fou))
fir.sort(key=lambda x: (x[1]+x[2], x[1], -x[0]), reverse=True)
sec.sort(key=lambda x: (x[1]+x[2], x[1], -x[0]), reverse=True)
thi.sort(key=lambda x: (x[1]+x[2], x[1], -x[0]), reverse=True)
fou.sort(key=lambda x: (x[1]+x[2], x[1], -x[0]), reverse=True)

result = fir + sec + thi + fou
for i in result:
    print('{} {} {}'.format(i[0], i[1], i[2]))
