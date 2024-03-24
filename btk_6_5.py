#break-continue ifadeleri
"""

name='Serkan Senturk'
for letter in name:
    if letter =='a':
        break
    print(letter) #a'ya kadar yazdırır a da durur

print()
for letter in name:
    if letter =='a':
        continue
    print(letter) #a'yı atlar a hariç hepsini basar

x=0
while x<5:
    if (x==2):
        break
    print(x)
    x+=1
#break yerine continue koyamayız çünkü 2 ye geldiğinde döngü en başa döner 1 arttırmadan 2 de taklılı kalır
"""
#1-100 e kadar tek sayıların toplamı

x=0
result=0
while x<=100:
    x+=1
    if x%2==0:
        continue
    result+=x

print(f"toplam: {result}")




