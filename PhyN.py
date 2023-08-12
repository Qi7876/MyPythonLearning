Index = int(input('请输入数列项数：'))

if Index == 1 or Index == 2:
    print('1')
else:
    a1 = a2 = 1

    for i in range(Index - 2):
        a1, a2 = a2, a1 + a2

    print(a2)
