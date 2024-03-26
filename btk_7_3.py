
#fonksiyon parametreleri
"""
def changeName(n):
    n='ada'
name= 'Serkan'

changeName(name)
print(name) #serkan

def change(n):
    n[0] ='istanbul'

sehirler=['ankara','izmir']
#change(sehirler)
#print(sehirler) #istanbul,izmir
n = sehirler  # sehirler [:] dersek elemanlarını n e kopyalar, n(0). indexini değiştirmek sehirleri etkilemez
n[0]='istanbul'
print(sehirler) #istanbul,izmir yine aynı sonuç
#bir adres göderip o adresteki bilgiyi güncelleriz
n = sehirler[:]
n[0]='aa'
print(sehirler)#istanbul,izmir
print(n) #aa,izmir
# orijinal listeyi bozmadan bu şekilde de yapılır

sehirler=['ankara','izmir']
change(sehirler[:])
print(sehirler) #ankara izmir ama n dedğişir

def add(a, b, c=0): # cye 0 demezsen ikili işlemi yapmaz
    return sum((a,b,c))
print(add(10,20)) #30
print(add(10,20, 30)) #60

def addi(*params):
    print(params[0]) #13
    return sum((params))

print(addi(13,34,56,56,9)) #istediğin kdar parametre girebilirsin
#sum fonksiyonunu kullanmak istemezsek

def addit(*paramss): #tuple için *
    sum=0
    for n in paramss:
        sum=sum+n
    return sum
print(addit(13,34,46,65,75))
"""
def displayUser(**args):#dicti. grlrcrğini belirtmek için **
    print(type(args)) #dict
    for key, value in args.items():
        print('{} is {}'.format(key,value))


displayUser(name='Serkan',age=26, city='Ankara')
displayUser(name='çınar',age=2, city='çorum', phone='123123')
displayUser(name='ada',age=6, city='istanbul', phone='123456', email='adaaaaa@gmail')

def myFunc (a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, key1='value1', key2='value2')