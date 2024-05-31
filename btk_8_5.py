
mylist=[1,2,3]
"""
myStr='my string'
print(len(mylist))
print(len(myStr))
print(type(mylist))
print(type(myStr))
"""
class Movie():
    def __init__(self,title,director, duration):
        self.title=title
        self.director=director
        self.duration= duration
        print("movie objesi oluşturuldu")
    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print("movie silindi")
m = Movie("film adı","yönetmen adı",120)
#print(len(m)) #len yok
#print(type(m)) #sonuç verir

print(mylist)
print(m) #movie object at5456767

#print(str(mylist)) #aynı sonuc
#print(str(m)) #film adı by yönetmen adı

print(len(mylist)) #3
print(len(m)) #eror len methodunu sonradan ekledik bu sayede 120 cevabını verdi

del m
print(m) #movie silindi
