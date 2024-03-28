#lamda fonksiyonları
"""

def square(num):
    return num**2

numbers=[1,3,5,9]
result=list(map(square, numbers))
for item in map(square,numbers):
    print(item)

print(result)

numbers=[1,3,5,9]
result=list(map(lambda num:num**2,numbers))
print(result)
square= lambda num:num**2
result=list(map(square,numbers))
print(result)
a=square(3)
print(a)
"""
numbers=[1,3,5,9,10]
#def check_even(num):
#    return num%2==0

check_even=lambda num:num%2==0

#result=list(filter(check_even,numbers)) #10
result=list(filter(lambda num:num%2==0,numbers))#10
result=check_even(numbers[2]) #false


print(result)