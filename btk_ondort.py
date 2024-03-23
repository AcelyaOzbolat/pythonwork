#3.18 dic örnekler
"""
students ={
    '120':{
        'name':'serkan',
        'surname':'senturk',
        'phone':'5280'
    },
    '125':{
        'name':'can',
        'surname':'korkmaz',
        'phone':'5281'
    },
    '128':{
        'name':'volkan',
        'surname':'al',
        'phone':'5282'
    },
}
"""
#yukarıdaki gibi olacak şekilde kullanıcıdan bilgileri al
#kullanıcıya öğrenci numarası sor bilgilerini yazdır
students={}
numbers=input("öğrenci no: ")
name= input("öğrenci adı: ")
surname=input("öğrenci soyadı: ")
phone=input("öğrenci tel: ")


"""
students[numbers]={
    'ad':name,
    'soyad':surname,
    'tel':phone
}
"""

#bu şekilde de olur
students.update({
    numbers:{
        'ad':name,
        'soyad':surname,
        'tel':phone
    }
})
numbers=input("öğrenci no: ")
name= input("öğrenci adı: ")
surname=input("öğrenci soyadı: ")
phone=input("öğrenci tel: ")

students.update({
    numbers:{
        'ad':name,
        'soyad':surname,
        'tel':phone
    }
})
numbers=input("öğrenci no: ")
name= input("öğrenci adı: ")
surname=input("öğrenci soyadı: ")
phone=input("öğrenci tel: ")

students.update({
    numbers:{
        'ad':name,
        'soyad':surname,
        'tel':phone
    }
})
ogrenciNo= input("öğrenci: ")
ogrenci=students[numbers]
print(ogrenci)#formatlı basacaksan {}içine yazarken{ogrenci['ad']} diye yaz


print(students)











