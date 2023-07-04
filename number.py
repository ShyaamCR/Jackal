i =1
x = 1

print('Hi')

for x in range(1,10000):
    print('x inside')
    for i in range(1,11):
        print('y inside')
        if x/i == 0:
            print('if insdie')
            i=+1
            print(x)
            continue
        else:
            x=+1
        


