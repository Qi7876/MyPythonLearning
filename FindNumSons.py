MotherNum = int(input('Please input the number: '))

for i in range(1, MotherNum + 1):
    if MotherNum % i == 0:
        print(i, ' ', end='')
