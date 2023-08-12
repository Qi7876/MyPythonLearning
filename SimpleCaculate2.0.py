WorkList = input('Please input two numbers and a operator:').split()
WrokCache = eval(WorkList[0] + WorkList[2] + WorkList[1])

if WorkList[2] == '+':
    print(eval(WorkList[0] + WorkList[2] + WorkList[1]))
elif WorkList[2] == '-':
    print(eval(WorkList[0] + WorkList[2] + WorkList[1]))
elif WorkList[2] == '*':
    print(eval(WorkList[0] + WorkList[2] + WorkList[1]))
elif WorkList[2] == '/':
    if int(WorkList[1]) == 0:
        print('Divided by zero!')
    else:
        print(eval(WorkList[0] + WorkList[2] + WorkList[1]))
else:
    print('Invalid operator!')

