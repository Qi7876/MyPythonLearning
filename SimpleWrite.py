TestFile = open('/\\TestFile.txt', 'w', encoding='UTF-8')

if TestFile.readlines == '':
    print('File is empty!')

TestFile.write('Hello World!\n')
print('Write Success!')
TestFile.close()
