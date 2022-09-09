a, pa, b, pb = input().split()
sa = ''
sb = ''
for i in range(len(a)):
    if a[i] == pa:
        sa += a[i]
for j in range(len(b)):
    if b[j] == pb:
        sb += b[j]
if sa or sb:
    if sa and sb:
        print(int(sa)+int(sb))
    elif sb:
        print(int(sb))
    elif sa:
        print(int(sa))
else:
    print(0)
