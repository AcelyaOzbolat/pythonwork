#örneklerrr
sayilar=[1,3,5,7,9,12,19,21]
"""
#1- sayılar listesindeki hangi sayılar 3ün katıdır
for sayi in sayilar:
    if (sayi%3==0):
        print(sayi)
    
#2- sayılar listesindeki sayıların toplamı kaçtır
toplam=0
for sayi in sayilar:
    toplam=toplam+sayi

print(toplam)

#3- sayılar listesindeki tek sayıların karesini al
for num in sayilar:
    if(num%2==1):
        result=num**2
        print(result)

sehirler=['kocaeli','istanbul','ankara','izmir','rize']

#4-şehirlerden hangileri en fazla 5 karakterlidir
for sehir in sehirler:
    if(len(sehir)<=5):
        print(sehir)
"""
urunler=[
    {'name':'samsung s6','price':'3000'},
    {'name':'samsung s7','price':'4000'},
    {'name':'samsung s8','price':'5000'},
    {'name':'samsung s9','price':'6000'},
    {'name':'samsung s10','price':'7000'}
]
#5- ürünlerin fiyatları toplamı nedir
toplam=0
for urun in urunler:
    fiyat=int(urun['price'])
    toplam+=fiyat
print(toplam)

for urunn in urunler:
    if int(urunn['price'])<=5000:
        print(urunn['name'])
