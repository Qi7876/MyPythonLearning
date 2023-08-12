year = input('Please input a year: ')

if int(year) % 4 == 0:
    print('This is a leap year.')
else:
    print('This is not a leap year.')

if int(year) < 1949:
    print('The PRC was not founded yet.')
elif (int(year) - 1949) % 10 == 0:
    print('This a big year.')
