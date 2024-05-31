#classlara method ekleme
"""
class Person:
    #class attributes
    address = "no information"

    #constructor(yapıcı method)
    def __init__(self, name, year):

        #object attributes
        self.name= name
        self.year=year

    #instance methods
    def intro(self):
        print("Hello there I am "+self.name)

    def calculateAge(self):
        return 2024-self.year



p1= Person('Serkan',1997)
p2=Person("Acelya",2002)
p1.intro() #hello there ı am serkan
p2.intro()

p2.calculateAge()
print(f"{p2.name}'nın yaşı:{p2.calculateAge()}") #acelyanın yaşı 22
print(f"{p1.name}'nın yaşı:{p1.calculateAge()}")
"""

class Circle:
    pi =3.14

    def __init__(self, r=1):
        self.r=r

    def cevreHesapla(self):
        return 2 * self.pi * self.r

    def alanHesapla(self):
         return self.r * self.r * self.pi


c1= Circle()  #r=1
c2 = Circle(5)

print(f"c1 alan: {c1.alanHesapla()} çevre: {c1.cevreHesapla()}")
print(f"c1 alan: {c2.alanHesapla()} çevre: {c2.cevreHesapla()}")