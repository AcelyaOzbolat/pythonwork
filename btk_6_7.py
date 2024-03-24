"""
for x in range(10):
    print(x)
#normal for formatında basar
number=[x for x in range(10)]
print(number) #[0,1,....9] liste şeklinde basar
"""
number=[]
for x in range(10):
    number.append(x)
print(number)#aynı liste şeklinde basar aynı sonuç

for y in range(10):
    print(x**2)

numbers=[x**2 for x in range(10)]
print(numbers) #her değerin karesi

numbers=[x*x for x in range(10) if x%3==0]
print(numbers)# 0,9,36,81
myString='hello'
myList=[]
for letter in myString:
    myList.append(letter)
print(myList) #['h',...

myList=[letter for letter in myString]
print(myList) #aynı sonuç

years=[1983,1998,1997,2002,1986]
ages=[2024-year for year in years]
print(ages) #[41,..

result=[x if x%2==0 else 'tek' for x in range(1,10)]
print(result)
#['tek',2,'tek',..

result=[]
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)#(0,0),(0,1),(0,2),(1,0)..

numbers=[(x,y) for x in range(3) for y in range(3)]
print(numbers) #aynı sonuç
