Target = int(input())
x = 1

while x <= Target:
    if Target % x == 0:
        print(x)
    x += 1
