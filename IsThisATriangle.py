TriangleSides = input('Please enter the three sides of a triangle: ').split()

if int(TriangleSides[0]) + int(TriangleSides[1]) > int(TriangleSides[2]) and int(TriangleSides[1]) + int(TriangleSides[2]) > int(TriangleSides[0]) and int(TriangleSides[2]) + int(TriangleSides[0]) > int(TriangleSides[1]):
    print('Yes')
else:
    print('No')