NumCount = int(input('请输入求和数个数；'))
Sum = 0

for i in range(NumCount):
    Sum += int(input('请输入第%d个数：' % (i + 1)))

print('求和结果为：%d' % Sum)