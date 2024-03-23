#for döngüsü

numbers=[1,2,3,4,5]
for num in numbers:
    print(num)
#listeden elemanı alır tek tek num a atar

for a in numbers:
    print('hello')        #5 kez hello yazar

names=['çınar','sadık','sena']

for name in names:
    print(f"my name is {name}")

isim='acelya serkan'
for n in isim:
    print(n)#string ifadeyi her karatkeri tek tek yazdırır

tuple=(1,2,3,4,5)
for t in tuple:
    print(t)#uine aynı şekilde aşağı doğru tek tek yazdırır
b= [(1,2),(1,3),(4,5)]

for c in b:
    print(c)

for x,y in b:
    print(x,y)

d={'k1':1,'k2':2,'k3':3}
for key,value in d.items():
    print(key,value) #bu şekilde ancak tamamını yazdırır


