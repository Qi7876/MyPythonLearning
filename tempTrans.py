temp = input('请输入温度：')

if temp[-1] in ['F', 'f']:
    C = (eval(temp[0:-1]) - 32) / 1.8
    print('转换后的温度是' + str(C) + 'C')
el4