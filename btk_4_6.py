#1- girilen bir sayının 0-100 arasında olup olmadığını kontrol et
"""
x=int(input('sayı: '))
result=(x>0)and(x<100)
print(f'sayı 0-100 arasındadır:{result}')

#2- girilen sayının pozitif çift sayı oldugunu kontrol ediniz
a=int(input('sayı: '))
result=(a>0)and(a%2==0)
print(f'girdiğiniz sayı çift ve pozitiftir:{result}')

#3-email ve parola bilgileri ile giriş kontrolu yapınız
mail='aciserkan@g.'
parola='abc'
m=input('mailiniz: ')
s=input('şifreniz: ')
result=(m=='aciserkan@g.') and(s=='abc')
print(f'giriş başarılı: {result}')

#4-girien 3 sayıyı büyüklük olarak karşılaştırın
a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))
result1=(a>b)
result2=(b>c)
result3=(a>c)
print(f'a b\'den büyüktür:{result1}')
print(f'b c\'den büyüktür:{result2}')
print(f'a c\'den büyüktür:{result3}')

#5- kullanıcıdan vize (%40) ve final(%60) notu al.Ort 50 den büyükse geçti yaz
vize=int(input('vize: '))
final=int(input('final: ')) 
ort=(vize*0.4)+(final*0.6)
if (ort>50):
    print(f'ortlamanız:{ort} geçtiniz')
else:
    print(f'ortlamanız:{ort} kaldınız')
"""
#kişinin ad, kilo, boy bilgilerini alıp kilo indekslerini hesaspla
ad=input('adınız: ')
boy=int(input('boyunuz: '))
kilo=int(input('kilonuz: '))
indeks=((kilo/boy)**2)    
#konuyla alakalı çözüm
if (indeks<18.4)and(indeks>0):
    print(f'indeksiniz:{indeks}. zayıf kategoridesiniz')
elif(indeks>18.4)and(indeks<24.9):
    print(f'indeksiniz:{indeks}. normal kategoridesiniz')
elif(indeks>25.0)and(indeks<29.9):
    print(f'indeksiniz:{indeks}. kilolu kategoridesiniz')
elif(indeks>30.0)and(indeks<34.9):
    print(f'indeksiniz:{indeks}. obez kategoridesiniz')
else:
    print('tekrar deneyiniz')
    
