NM = input('请输入n m: ').split()
n, m = int(NM[0]), int(NM[1])

for x in range(1, n + 1):
    for y in range(x + 1, n + 1):
        if m % (x + y) == 0:
            print('({0}, {1})'.format(x, y))
            break
