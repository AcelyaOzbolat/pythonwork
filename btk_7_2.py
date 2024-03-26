#fonkiyon kullanımı
"""
def sayHello():
    print("Hello")

sayHello() # Hello

def sayHello(name="user"):
    print("Hello "+ name)

sayHello("Serkan") # Hello serkan
sayHello() # Hello user
# paramertreyi ya defli kısma tanımlıycaz ya da fonksiyonu çağırırken
"""
def sayHello(name="user"):
    return "Hello "+ name
msg=sayHello("Serkan")
print(msg) #defin içinde print kullanmadan bu şekilde olur hello serkan


def total(num1,num2):
    return num1+num2
result=total(10,20)
print(result)

def yasHesapla(dogumyili):
    return 2024-dogumyili

ageSerkan=yasHesapla(1997)
print(ageSerkan)

def emeklilik(dogumYili, isim):
    yas=yasHesapla(dogumYili)
    emek=65- yas

    if emek>0:
        print(f"emekliliğinize {emek} yıl kaldı")
    else:
        print("zaten emekli oldunuz")
emeklilik(1983, 'serkan') # emeklilliğinize 24 yıl kaldı