#örnekler
numbers=1,5,7,10,6
x,y,z=2,5,107
"""
#1- kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir
a=input("ilk sayı: ")
b=input("ikinci sayı: ")
result=(int(a)*int(b))-(x+y+z)
print(result)

#2-y'nin x'e kalansız bölümünü hesaplayın
y //=x
print(y)
"""
#3- (x,y,z) toplamnın mod 3 ü nedir
toplam=(x+y+z) 
result =toplam % 3

#4- y'nin x. kuvvetini hesapla
y**=x
print(y)

#5- x,*y,z =numbers işlemine göre z'nin küpü kaç
x,*y,z=numbers
z**=3
print(z)

#6- x,*y,z =numbers işlemine göre y'nin değerleri toplamı kaç
result=y[0]+y[1]+y[2]
print(result)





