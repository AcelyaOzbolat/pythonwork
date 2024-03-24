"""
#range
for item in range(10):
    print(item)
    #0 dan başlar 9 a kadar yazdırır

for a in range(10,20,5):
    print(a)
    #10,15 (başlangıç,bitiş,kaçar kaçar)
print(list(range(10,50,5))) #liste biçiminde yazar

#enumerate
index=0
greeting='hello there'

for letter in greeting:
    print(f'index:{index} letter:{letter}') #letter:{greeting[index]} diye de yazılabilir
    index +=1

greeting='hello there'
for index,letter in enumerate(greeting):
    print(f'index:{index} letter:{letter}')


for item in enumerate(greeting):
    print(item) #(0, 'h')...
"""
#zip methodu
list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
print(list(zip(list1,list2))) #iki listeyi birbirine eşitler.[(1,'a'),...
#eşitlenene kadar yazar biri fazlaysa fazla olanı basmaz

for item in zip(list1,list2):
    print(item) #alt alta yazar
for a,b in zip(list1,list2):
        print(a,b)
