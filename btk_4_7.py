#Identity & Membership operators
#Identity operator:is
"""
x=y=[1,2,3]
z=[1,2,3]
print(x==y) #true
print(x==z) #true
print(x is y) #true
print(x is z) #false

x=[1,2,3]
y=[2,4]
print(x is y)#false
del x[2]
y[1]=1
y.reverse()
print(x)#1,2
print(y)#1,2
print(x is y) #false
print(x==y)#true
print(x is not y)#true
"""
#membership operator:in
x=['apple','banana']
print('banana' in x) #true
name= 'çınar'
print('a' in name)#true
print('o' not in name) #true



