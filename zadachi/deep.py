a=int(input())
b=int(input())
c=int(input())
d=int(input())
if  not (1<=a<=3):
    print('Неверная зона')
elif a==1:
    a1=50
elif a==2:
    a1=80
elif a==3:
    a1=120
if not(0<=b<=23):
    print('Неверное время')
elif 6<=b<=9 or 17<=b<=19:
    b1=1.2
else:
    b1=1
if 1>c:
    print('Неверное количество')
if d==1:
    d1=0.9
else:
    d1=1
print(a1*b1*c*d1)