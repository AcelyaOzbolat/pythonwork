#ınheritance (katılım):miraz alma

#person => name, lastname, age, run(), eat(), drink()  ...
#student(person), teacher(person)

#animal=> dog(animal),cat(animal)
class Person():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print("Person created")
    def Who_am_i(self):
        print("I am a person")
    def Eat(self):
        print("ı am eating")

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname) # personu tekrar çalıstırır
        self.number = number
        print("Student created")
    def Who_am_i(self):
        print("ı am a student")

    def SayHello(self):
        print("hello ı am a student")


class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch
    def Who_am_i(self):
        print("ı am a teacher")



p1= Person("ayşe ", "ayşe") #person created
s1=Student("acelya ", "serkan",  12)  #student created

print(p1.fname + p1.lname)
print(s1.fname + s1.lname +str(s1.number))

p1.Who_am_i()  #ı am a person
s1.Who_am_i()  #
#aynıı isimde methodlar ama farklı sınıflarda
p1.Eat()
s1.Eat()

s1.SayHello()

t1=Teacher("ayça", "yılmaz", "math")

t1.Who_am_i()