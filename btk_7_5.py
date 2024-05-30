#lamda expressions, Map, Filter

"""

def square(num):
    return num**2

#def square(num): return num**2
#bu şekilde de yazabilirsin
num=int(input("enter the number:"))
result= square(num)
print(f"Your result is: {result}")
"""
"""
def square(num): return num ** 2

numbers=[1,3,5,7,9]
result=list(map(square, numbers)) #list olmadan run edersen adres bilgisi verir
#alternatif olarak for döngüsü kullan
for item in map(square, numbers):
    print(item)


print(result)
"""
"""
numbers=[1,3,5,9]
result=list(map(lambda num: num **2,numbers))
print(result)  #[1,9,25,81]
"""
"""
square = lambda num: num**2
numbers=[1,3,5,7,9]
result=list(map(square, numbers))
print(result)#1,3,5,7,9
result1=square(2)
print(result1) #4
"""
"""
square=lambda num: num**2
numbers=[1,3,5,7,9,4,6]
def check_even(num): return num%2==0
result=list(filter(check_even, numbers))
print(result)
"""
"""
numbers=[1,3,5,7,9,4,6]
def check_even(num): return num%2==0

#result=list(filter(check_even, numbers)) #4,6
result=list(filter(lambda num: num%2==0, numbers)) #4,6
print(result)
"""

numbers=[1,3,5,7,9,4,6]
check_even= lambda num: num%2==0

result=list(filter(check_even, numbers)) #4,6
print(result)
result1= check_even(numbers[2])
print(result1) #false
