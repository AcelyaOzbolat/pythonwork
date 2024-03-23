names = ['Serkan', 'Acelya', 'Deniz', 'Hakan']
years = [1998, 2000, 1998, 1987]
"""#'cenk ismini sona ekle
names.append('cenk')
#sena ismini başa getir
names.insert(0,'sena')
#deniz ismini sil
names.remove('Deniz') #pop da kullanabilirsin ama index belirtmen lazım

#deniz ismminin indexi nedir
index = names.index('Serkan')
print(index)
names.pop(index)  #serkanı siler
#ali listenin elemanı mı
result= 'Serkan' in names
print(result) # true
#liste elemanlarını ters çevir
names.reverse()
#liste elemanlarını alfabetik sırala
names.sort()
years.sort()
# str= "chevrolet,dacia" karakter dizisini listeye çevir
str= "chevrolet,dacia"
result=str.split(',')
print(result)
# en düşük eleman
min=min(years)
max=max(years)
print(min,max)
#years dizisinde kaç tane 1998 vardır
a=years.count(1998)
print(a)
#years dizisinin tüm elemanlarını silin
years.clear()

print(years)
print(names)
"""
#kullanıcıdan uc tane marka bilgisi al listede sakla
markalar = []
marka=input("marka: ")
markalar.append(marka)
marka=input("marka: ")
markalar.append(marka)
marka=input("marka: ")
markalar.append(marka)
print(markalar)
