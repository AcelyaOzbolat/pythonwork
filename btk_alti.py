#3.9. video sorular
website='https:www.aciserkan.com'
course ='python kursu: sıfırdan ileri derecede python'
"""
#1-'course' karakter dizisinde kaç karakter vardır
print(len(course))
length= len(course)
print(length)

#2- website içinden www karakterlerini alın
print(website[6:9])

#3- website içinden com karakterlerini alın
print(website[20:23])

#4-course içinden ilk 15 ve son 15 karakterlerini alın
print(website[:15])
print(website[8:23])
print(website[-15:])

#5- course ifadesindeki karakterleri tersten yazdırın
print(course[::-1])
"""
s= '12345'*5
print(s)
print(s[::5]) 
#ilk boiluk nereden başladığı index sayması yap
#ikinci nerede biteceği normal say, 3. ise kaçar kaçar gideceği normal say saydığını da al

name, surname, age, job= 'acelya','senturk', 22, 'yazilimci'
#yukarıda verilen değişkenler ile ekrana aşağıdai ifadeyi yazdırın
#'benim adım acelya senturk. yaşım 22 ve mesleğim yazilimci.'
print(f"benim adım {name} {surname}. yaşım {age} ve mesleğim {job}.")

#7- Hello world ifadesindeki w harfini W ile değiştir
a='hello world'
a= a[0:6] + 'W' + a[7:]
print(a)

#8- 'abc'ifadesini üç kez yazdır
b= 'abc'*3
print(b)
