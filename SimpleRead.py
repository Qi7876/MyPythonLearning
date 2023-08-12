TestFile = open("TestFile.txt", "r")
Content = TestFile.readlines()

for i in Content:
    print(i.strip())
