#3.16 tuple
list=[1,2,3]
tuple=(1,'iki',3)
"""
print(type(list)) #liste
print(type(tuple)) #tuple

print(list[2])#3
print(tuple[2])#3
print(len(tuple))#3
print(len(list)) #3

list[0]='serkan' #değiştirir
tuple[0]='aci' #hata verir tupleda eleman değiştiremezsin
#tuple=(..) deyip yeni liste verebiliriz ama tek tek değiştirmez silme yapılamaz
"""
print(tuple.count('ayse'))

print(tuple.index('iki'))
names=('serkan','aci','cınar')+tuple 
names.remove('aci')#hata verir
print(list)
print(tuple)
print(names)