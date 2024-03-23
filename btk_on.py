#3.13 örnekler
#3.14
numbers=[1,12,5,16,4,9,10]
letters=['a','g','s','b','y','a','s']
val=min(numbers)
val=max(numbers)
val=max(letters) #y
val=min(letters) #a

val=numbers[3:6] #16,4,9
val=numbers[:3] #1,12,5
print(val)

numbers[4]=40


numbers.append('49')  #en sona ekler
numbers.insert(3, 78) #index saymasıyla 2 ve 3. indexin arasına 78 ekledi 5,78,16
numbers.insert(-1,52) #..52,49

numbers.pop() # en sondakini siler
numbers.pop(0) #0. indexi siler
#numbers.pop(-1) # en sondakini siler

numbers.remove(9) #silmek istediğin elemanı siler

numbers.sort() #küçükten büyüge sıralar
letters.sort() #alfabetik olarak sıralar
numbers.reverse() #tersine sıralar
print(len(numbers))

print(numbers.count(10)) #yazdıgın elemandan kaç tane oldugunu söyler
print(letters.count(10)) #0

numbers.clear() #tüm elemanları siler
print(numbers)


