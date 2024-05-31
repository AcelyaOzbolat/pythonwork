#3.19 sets
"""
fruits = {'orange', 'apple', 'banana'}
print(fruits) # fruits[0] idexleemez hata verir

for x in fruits:
    print(x)
#tek tek yukarıdan aşağı yazar
fruits.add('cherry') #tek bir elean eklerken
fruits.update(['mango','grape']) #çoklu eklersen liste şeklinde eklersin
#aynı elemanı ikinci kez eklediğinde bir kez yazar 2 değil

myList= [1,2,5,4,4,2,1]
print(set(myList)) #set tekrarlayan elemanları siler

fruits.remove('mango') #mangoyu sildi
fruits.discard('apple') #bu şekilde de siler
fruits.pop()  #rastgele bir eleman siler
fruits.clear()

print(fruits)   
"""
##########################################
#3.20 value & Reference types ==== int ve str
"""
x=5
y=25
x=y
y=10
print(x,y) #25 10
"""
#reference types === list

a =['apple','banana']
b=['apple','banana']
a=b
b[0]='orange'
print(a,b) #orange, apple.orange, apple basar
#listelerde a=b yaptığımza adresi aynı olur


