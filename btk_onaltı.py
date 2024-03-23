#4.1 atama operatörleri

x, y, z= 5, 10, 20
"""
#x,y= y,z
#x= x+5
x+=5
x-=5
x*=5
#x/=5#5.0
#x%=5#0.0
x//=5  #bölmede tam kısmı verir
y**=3 #1000

print(x,y,z)
"""
values=1,2,3,4,5
print(values)
print(type(values)) #tuple
#x,y,z=values #1,2,3
#değer sayıları eşit olmalı hata verir
#çoksa eğer
x,y,*z=values #1,2,[3,4,5]
print(x,y,z[0])#1,2,3

print(x,y,z)

