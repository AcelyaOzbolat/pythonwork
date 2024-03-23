"""
#1- kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip 
#ehliyet alabilme durumunu kontrol ediniz. Ehliyet
#alma koşulu en az 18 ve eğitim durumu lise ya da üni olmalıdır

name =input('isminiz: ')
age=int(input('yaşınız: '))
okul=input('eğitim durumunuz: ')

if (age>=18):
    if(okul=='üni'):
        print(f'{name} ehliyet alabilirsin')
    elif(okul=='lise'):
        print(f'{name} ehliyet alabilirsin')  
    else:
        print(f'{name}, lise mezunu olmalısın')      
else:
    print('yaşınız yetersiz.')        

#(age>=18) and(eğitim=='lise')or (eğitim=='üni')    

#2- bir öğrencinin 2 yazılı 1 sözlü notunu alıp hesaplanan 
#ortalamaya göre not aralığına karşılık gelen not bilgisini yazdır
yazili1= int(input('1. yazılı notu: '))
yazili2= int(input('2. yazılı notu: '))
sözlu= int(input('sözlü notu: '))
ortalama=(yazili1+yazili2+sözlu)/3
if (0<=ortalama)and(ortalama<=24):
    print(f'not ortalamanız:{ortalama}')
    print(f'harf notunuz: F')
elif (25<=ortalama)and(ortalama<=44):
    print(f'not ortalamanız:{ortalama}')
    print(f'harf notunuz: E')    
elif (45<=ortalama)and(ortalama<=54):
    print(f'not ortalamanız:{ortalama}')
    print(f'harf notunuz: D')    
elif (55<=ortalama)and(ortalama<=69):
    print(f'not ortalamanız:{ortalama}')
    print(f'harf notunuz: C')    
elif (70<=ortalama)and(ortalama<=84):
    print(f'not ortalamanız:{ortalama}')
    print(f'harf notunuz: B')    
elif (85<=ortalama)and(ortalama<=100):
    print(f'not ortalamanız:{ortalama}')
    print(f'harf notunuz: A') 
else:
    print('geçersiz giriş yaptınız')

#3- trafiğe çıkış tarihi alınan bir aracın servis zamanını hesaplayın

days=int(input('gün: '))

if days<=365:
    print('birinci servis aralığı')
elif days>365 and days<=365*2:
    print('ikinci servis aralığı')    
elif days>365*2 and days<=365*3:
    print('üçüncü servis aralığı')
else:
    print('hatalı giriş')

###ya da
import datetime
tarih= input('aracınız hangi tarihte trafiğe çıktı: ')
tarih=tarih.split('.')

trafigeCikis=datetime.datetime(tarih[0],tarih[1],tarih[2])
simdi= datetime.datetime.now()
fark=simdi-trafigeCikis
days=fark.days

if days<=365:
    print('birinci servis aralığı')
elif days>365 and days<=365*2:
    print('ikinci servis aralığı')    
elif days>365*2 and days<=365*3:
    print('üçüncü servis aralığı')
else:
    print('hatalı giriş')
"""