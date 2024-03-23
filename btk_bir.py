print(2+2)
print(type(3))

# örnek
maasAli= 5000
maasAhmet= 4000
vergi=0.27
print(maasAli-(maasAli*vergi))
print(maasAhmet-(maasAhmet*vergi))

#DEĞİŞKEN TANIMLAMA KURALLARI
#rakam ile başlayamaz
number= 3
number-= 10
print(number)
#büyük küçük harf duyarlılığı vardır
#türkçe karakter kullanılmaz
a='10'
b='20'
print(a+b) # a ve b yi string olarak algılar sonuç 1020 olur

name= 'serkan'
surname='şentürk'
print(name +'\t'+ surname)   #(name+' '+surname)

#x, y, name1, isStudent =(1, 2.3, "çınar", True)
#tek bir satırda birden çok ve farklı türde değişken tanımlanabilir
# tanımlarken değişkenler arasına bosluk konmaz

#ders 3.4
#ÖRNEK
"""
1- bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

müşteri adı
müşteri soyadı
müşteri ad+soyad
...
"""
musteriAdi= 'Serkan'
musteriSoyad='Şentürk'
musteriAdSoyad= musteriAdi+' '+musteriSoyad
musteriCinsiyeti= True
musteriTC=123456789
musteriDG=1997
musteriYasi= 2024-musteriDG
print("yas:",musteriYasi)

"""
ÖRNEK
ŞİPARİŞLERİN TOPLAMI KAÇTIR
"""
order1=110
order2=1100.5
order3=356.95
total=order1+order2+order3
print("toplam:",total)


