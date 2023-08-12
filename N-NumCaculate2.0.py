Times = int(input("请输入你要计算的组数："))

for i in range(Times):
    print('第%d组数据' % (i + 1))
    NumCount = int(input("请输入你要计算的数字个数："))
    Sum = 0
    for a in range(NumCount):
        Sum += int(input())
    print('计算结果为 %d' % Sum)
