num = str("{:0>4}".format(input()))
while True:
    ac = str().join(sorted(num))
    dec = ac[-1::-1]
    num = "%04d" % (int(dec)-int(ac))
    print("%s - %s = %s" % (dec, ac, num))
    if num in ('0000', '6174'):break
