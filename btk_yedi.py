#3.10
message ='Hello there. My name is Acelya Senturk'
"""
print(message)  #Hello there. My name is Acelya
message = message.upper()  #HELLO THERE....
print(message)
message = message.lower() #hello there....
print(message)
message = message.capitalize() #Hello there... sadece en baştaki karakter büyük olur
print(message)
message = message.title() # tüm kelimelerin başı buyuk olur
print(message)

print(message) 
message=message.strip()  #başta boşluk karakteri varsa yok eder
print(message)

message=message.split()  #'Hello', 'there'.... diye ayırır.her boiluktan sonrası ayrı eleman olur
print(message[0]) #bu durumda 0. index hello olur 
message=' '.join(message) #eski haline çeirir

message=message.split('.')
print(message) # noktaya göre ayırır


message.find('Acelya') #ilk index numarasını verir
print(index)

isFound= message.startswith('H') # true verir
print(isFound)

isFound= message.endswith('d')  #false
print(isFound)

message= message.replace('Acelya','Senturk') #acelya yerine senturk yazar
print(message)
message= message.replace(' ','*').replace('a','u') #boşluk yerine * koyar
"""

message= message.center(100) #         hello .....
message= message.center(100,'*') #************ h3llo....**********

print(message)