from random import *
a = randint(4, 31)
s = 0
print('v kuche '+str(a)+' kamney')
while a > 4:
    if a == 1:
        print('Vi pobedili')
    elif a==2:
        print('bot ubral 1 kamen i pobedil')
    elif a == 3:
        print('bot ubral 2 kamnya i pobedil')
    elif a == 4:
        print('bot ubral 3 kamnya i pobedil')
    else:
        s = randint(1, 4)
        a = a-s
        print('bot ubral '+str(s)+' kamney')
        print('Ostalos '+str(a)+' kamney')
        print('vedite cislo kamney')
        b = int(input())
        a = a-b
        print('Ostalos ' + str(a) + ' kamney')
if a == 1:
    print('Vi pobedili')
elif a==2:
    print('bot ubral 1 kamen i pobedil')
elif a == 3:
    print('bot ubral 2 kamnya i pobedil')
elif a == 4:
    print('bot ubral 3 kamnya i pobedil')
