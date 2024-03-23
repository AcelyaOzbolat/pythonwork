#örnekler
"""
sayilar=[1,3,5,7,9,12,19,21]

#sayialr listesini while ile ekrana yazdırın
i=0
while(i<len(sayilar)):
    print(sayilar[i]) 
    i += 1

#başlangıç ve itiş değerini kullanıcıdan alıp aradaki tüm tek sayıları yazdır
baslangic = int(input('başlangıç sayısı: '))
bitis = int(input('bitiş sayısı: '))
i=baslangic
while(i<bitis):
    i+=1
    if i%2==1:
        print(i)
    

#1-100 arasındaki sayıları azalan şekilde yazdırın
i=100
while i>0:
    print(i)
    i-=1


#kullanıcıdan aldığınız 5 sayıyı ekranda sıralı bir şekilde yazdırın

numbers=[]
i=0

while i<5:
    sayi=int(input('sayı: '))
    numbers.append(sayi)
    i+=1
numbers.sort()
print(numbers)
"""
#kullanıcıdan alacağınız ürün bilgisini ürünler listesinde saklayın
urunler=[]

adet =int (input('kaç adet ürün:'))
i=0
while i<adet:
    name=input('ürün adı: ')
    price=input('ürün fiyatı: ')
    urunler.append({
        'name':name,
        'price':price
    })
    i+=1
for urun in urunler:
    print(f'ürünün adı:{urun["name"]}. ürünün fiyatı:{urun["price"]}')    
