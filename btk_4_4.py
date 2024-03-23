"""
# girilen iki sayıdan hangisi büyüktür
a=int(input("ilk sayı: "))
b=int(input("ikinci sayı: "))
result= (a>b)
print(f"a:{a} b:{b}den büyüktür:{result}")

#kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ort hesaplat
#ort 50 üzerindeyse geçti yaz
v= float(input("vize: "))
f=float(input("final: "))
result=((v*0.6)+(f*0.4))
print(f'puanınız:{result}. dersten geçtin mi:{result>50}')

#girilen sayı tek mi çift mi yazdır
sayi= int(input("sayı: "))
tekcift=(sayi%2==0)
print(f"girilien sayı çift:{tekcift}")

#girilen sayı negatif mi pozitif mi yazdırın
sayi=int(input("sayı: "))
pozitifmi= (sayi>0)
print(f"girilen sayı pozitif:{pozitifmi}")
"""
#parola ve email bilgisini isteyip doğruluğunu kontrol edin
#(email: email@sadikturan.com  parola:abc123)
email='email@sadikturan.com'
password='abc123'
girilenmail =input('mail:')
girilenp=input("şifre: ")
ismail=(email==girilenmail.lower().strip())
ispas=(password==girilenp.lower().strip())
print(f"mail doğru mu:{ismail}. Parola doğru mu:{ispas}")












