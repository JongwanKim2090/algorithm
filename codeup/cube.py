n, m = input().split()

for x in range(1, int(n)+1):
    for y in range(1, int(m)+1):
        print(x, y)


a = int(input(), 16)

for m in range(1, 16):
    print('%X'%a, '*%X'%m, '=%X'%(a*m), sep='')