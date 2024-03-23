#mantıksal operatörler
x=5
hak=5
devam='e'

result= 10>x>5
#print(result) #false

#and
#true,true=> true  
#true,false=>false
result= (x>5) and (x<10)
print(result) #false
a=(hak>0)and(devam=='e')
print(a)#true

result=(x>0) and(x%2==0)
print(f'sayı çift ve pozitif:{result}')

#or
#true,false=>true yalnızca false,false=>false
result=(x>0) or (x%2==0)
print(f'sayı çift veya pozitif:{result}')

result=not(x>0) or (x%2==0)
print(f'sayı çift veya pozitif:{result}') #false

result=((x>5)or(x<10)and(x%2!=0))
print(result)#true











