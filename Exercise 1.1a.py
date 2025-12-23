# This is a program which finds if the triangle is possible by inputting 3 of it's sides

a, b, c = int(input()), int(input()), int(input());



if a == b == c:
    print('triangle is possible')
elif a == b or a == c or b == c:
    if (a + b)>=c or (a+c)>= b or (b+c)>= a:
        print('triangle is possible')
    else:
        print('triangle is impossible')
elif a**2 == b**2 + c**2:
    print('triangle is possible')
elif a**2 > b**2 + c**2:
    print('triangle is impossible')
elif b**2 == a**2 + c**2:
    print('triangle is possible')
elif b**2 > a**2 + c**2:
    print('triangle is impossible')
elif c**2 == a**2 + b**2:
    print('triangle is possible')
elif c**2 > a**2 + b**2:
    print('triangle is impossible')
else: 
    print('triangle is impossible')
    

    
    
    
 
    
#print(a, b, c)
