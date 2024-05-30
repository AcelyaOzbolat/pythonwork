#Global ve Local Değişkenler
#global scope
x= 'global x'

def function ():
    #local scope
    x = 'local x'
    print(x)  #local x
function()
print(x)  #global x

#global olarak tanımlanan serkan
name ="Serkan"
def change_name(new_name):
    #local
    name=new_name
    print(name) #acelya

change_name('Acelya')
print(name) #serkan

name1= "global string"

def greeting():
    name1 = 'cinar'
    def hello():
        print('hello '+name1) #hello cinar
    hello()

greeting()
print(name1) #global string


x=100
def test(x):
    print(f"x: {x}") # x:100
    x=200
    print(f"x changed to {x}") # changed to 200

test(x)
print(x)  #100
print()
# yani fonksiyonla bu şekilde değiştiremeyiz
#bunun için aşağıdaki
# fonkisyondaki ve çağırırken parantezdeki değişkeni sil
a=100
def test():
    global a #global a üzerine yaptığın her işlem dışarıdaki a yı da etkiliyor
    print(f"a: {a}") # a:100
    a=200
    print(f"a changed to {a}") # changed to 200

test()
print(a)  #200

