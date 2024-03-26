
#girilen bir sayının asal sayı olup olmadığını kontrol et

number=int(input("enter a number: "))
if (number==1):
    print("sayı asal değildir")
asalmi = True

for i in range(2,number):
    if(number%i==0):
        asalmi=False
        break
if asalmi:
    print("sayı asaldır")
else :
    print("sayı asal değildir")


