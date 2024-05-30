# ÖRNEK- BANKAMATİK

SerkanHesap = {
    'ad': 'Serkan Şentürk',
    'hesapNo': '12345678',
    'bakiye': 3000,
    'ekHesap': 2000
}
AcelyaHesap = {
    'ad': 'Açelya Şentürk',
    'hesapNo': '12343456789',
    'bakiye': 2000,
    'ekHesap': 1000
}
def paraCek(hesap, miktar):
    print(f"merhaba {hesap['ad']}")


    if hesap['bakiye']>= miktar:
        print("paranızı alabilirsiniz.")
    else:
        toplam= hesap['bakiye'] + hesap['ekHesap']

        if(toplam>=miktar):
            ekhesapkullanımı=input('ek hesap kullanılsın mı (e/h)')

            if ekhesapkullanımı=='e':
                print('paranızı alabilirsiniz.')
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} tl bulunmaktadır")
        else:
            print("üzgünüz bakiye yetersiz")


miktar=int(input("çekmek istediğiniz para miktarı: "))
paraCek(SerkanHesap, miktar)
