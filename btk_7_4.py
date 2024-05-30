"""
# 1- gönderilen kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız
def yazdir(kelime, adet):
    print(kelime*adet)

ne=input('söylemek istediğiniz kelime: ')
kaç= int(input('kaç adet söylensin:'))
yazdir(ne\n, kaç)


#kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren bir fonk yaz
def listeyeCevir(*args):
    liste=[]

    for param in args:
        liste.append(param)
    return liste
result= listeyeCevir(10,20,30,40,'merhaba')
print(result)

#gönderilen iki sayı arasındaki sayıların asallık durumu
sayi1=int(input("sayı: "))
sayi2=int(input("sayı: "))

def asalSayilariBul(sayi1,sayi2):

    for sayi in range(sayi1,sayi2+1):
        if sayi >1:
            for i in range(2,sayi):
                if(sayi%i==0):
                    break
                else:
                    print(sayi)


asalSayilariBul(sayi1,sayi2)
"""

#kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde yaz
def tamBolenleriBul(sayi):
    tamBolenler=[]
    for i in range(2,sayi):
        if(sayi%i==0):
            tamBolenler.append(i)
    return tamBolenler

sayi=int(input("ssayı:"))
print(tamBolenleriBul(sayi))
