N = int(input('Enter N: '))
M = int(input('Enter M: '))
Counter = 0

for Num1 in range(1, N + 1):
    for Num2 in range(Num1 + 1, N + 1):
        if Num1 + Num2 == M:
            print('({0}, {1})'.format(Num1, Num2))
            Counter += 1

print(Counter)
