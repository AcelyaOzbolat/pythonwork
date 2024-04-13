x = 'global x'
def function():
    x= 'local x'
    print(x)
function()  #local x

print(x)  #global x

name='serkan'

def changeName(new_name):
    name=new_name
    print(name)
changeName('acelya')  #acelya

name='global string'

def greeting(name):
    name='serkan'
    def hello():
        print('Hello '+name)
    hello()

greeting('acelya') #hello serkan

x=50
def test():
    #global x dersek dışarıdaki x de 100 olur
    print(f'x:{x}') #50
    x=100
    print(f'x in yeni değeri: {x}') #100

test()
