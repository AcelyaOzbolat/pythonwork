#class
#object

class Person:
    #class attributes
    adsress ='no information'
    #oject attributes

    #constructor (yapıcı metod)
    def __init__(self, name, year):  #init yapıcı metottur. persondan herhangi bir şey ürettiğin anda init çalısır
        self.name = name
        self.year = year
        print('init methodu çalıstı')

    #methods
a=0
if a > 10:
    pass  #hiçbir şey yazmayacağın durumda hata vermez
#p1 ve p2 için iki kez init çalısır
#object (instance)

p1 = Person('Serkan', 1997)
print(p1) #p1 in adresini verdi person tipi oldugunu da der
p2 = Person( name ='Acelya',year= 2002) #bu şekilde de tanımlanabilir

print(type(p2)) #class ..main...Person
print(p1 == p2) #false
print(f"name: {p1.name} year: {p1.year} adrres: {p1.adsress}") #name : serkan year :1997 adres: no informaiton
print(f"name: {p2.name} year: {p2.year}")

p1.name='Alparslan' #bu şekilde değiştirebilirsin
p1.adsress='Ankara'
# accessing object attributes
print(f"name: {p1.name} year: {p1.year} adrres: {p1.adsress}") #name : alparslan year :1997 adres: ankara
print(f"name: {p2.name} year: {p2.year}")




