#sayı tahmin oyunu
#1-100 arasında rastgele sayı üretilecek bir sayıyı aşağı yukarı ifadeleriyle buldurmaya çalısın

import random
sayi = random.randint(1,50)
hak=10
while hak>0:
    hak-=1
    tahmin=int(input('tahmin: '))

    if sayi==tahmin :
        print('doğru tahmin!!!')
        sayi+=9
        hak+=5
        continue
    elif sayi>tahmin:
        print("çık...")
    else:
        print("in...")

    if hak==0:
        print("Tahmin hakkınız bitti")
        continue
