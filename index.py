#STRİNGS
#print("serkan's home")
#print("""serkan 
#aci
      
#?""")
#print("hello\n world")     #\n bir alt satıra geçer
#print("hello\tworld")      #\t boşluk koyar

#message="hi world"
#print(message)

#m1,m3="hello"," hi"  
#m2=" world" 
#print(m1 + m2 + m3)
#print(m1 + " "+ m2)


message1="Merhaba"
message2="world"
#print(message1[3])                #tek tek sayı yazıp istediğin elemanı çekebilirsin
#print(message1[0:3])              #0.indexten 3.indexe e kadar alır 3 dahil olmaz
#print(message1[::])               #hepsini basar
#print(message1[::2])              #ilk indexi aldı, aldıgı indexten sonra 2. ye denk geleni yazdırır çıktı:mraa
#print(message1[::-1])             #tersten yazdırır
#print(message1[::-2])             #tersten ilk indexi alıp tersten 2.ye denk geleni yazdırır çıktı:aarm
#print(message1.upper())           #hepsini büyük harf yapar
#print(message1.lower())           #hepsini küçük harf yapar
#message1=message1.upper()         #kalıcı olarak büyük yapar
#print(message2.capitalize())      #baş harfini büyütür
#print(message1.startswith("me"))  #false verir
#print(message1.startswith("Me"))  #true verir
#print(message1.endswith("a"))     #true
#print(len(message1))              #7
#print(len(message1+message2))
#print("hello "*10)           #10 tane hello yazar
 
name="Açelya"
age="6"
#print("{}, {} yaşindadir".format(name,age))   ##############################################
print(f"{name} {message1} dedi")
print(f"{name} {age}")








