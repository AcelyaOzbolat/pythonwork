#3.8
surname='Senturk'
name='Serkan'
"""
print("My name is {}".format(name))
print("I am {} {}".format(name,surname))
print("I am {1} {0}".format(name,surname)) #ı am senturk serkan
"""
age=26
"""
print("I am {} {}. And I am {} years old.".format(name,surname,age))
print("I am {n} {s}. And I am {a} years old.".format(n=name,s=surname,a=age))
print("I am {} {}. And I am {} years old.".format(name,surname,'26'))



result=200/700
print("the result is: {r:1.3}".format(r=result)) #0.286

print("the result is: {r:7.3}".format(r=result)) #  0.286  7 başta bırakacğı boşluk 3 ise virgülden sonra yazdırdığı basamak
"""
print(f"My name is {name} {surname} and ı am {age}")

