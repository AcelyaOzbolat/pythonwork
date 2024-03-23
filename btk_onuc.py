#3.17 dictionary
#key-value  19=> çorum

cities=['kocaeli', 'istanbul']
plakalar =[41, 34]
"""
print(plakalar[cities.index('kocaeli')])   #41
print(plakalar[cities.index('istanbul')])  #34 yazar

plakalar={'kocaeli':41, 'istanbul':34}  #{'key':'value'}
print(plakalar['kocaeli'])
print(plakalar['istanbul'])

plakalar['ankara']=6
print(plakalar) #{'kocaeli':61....'ankara':6}
plakalar['kocaeli']='new value' #61le new value yu değiştirdi
#yeni eleman eklenir, değişiklik yapılabilir
print(plakalar)
"""
users={
    'acelyaSenturk':{
        'age':22,
        'roles':['admin'],
        'mail':'abc',
        'adres':'ankara',
        'phone':5219
    },
    'serkanSenturk':{
        'age':26,
        'roles':['admin','boss'],
        'mail':'bcd',
        'adres':'kalbim',
        'phone':'5280'
    
    }
}
print(users['serkanSenturk'])
print(users['serkanSenturk']['age']) #26
print(users['serkanSenturk']['roles'])#admin, boss
print(users['serkanSenturk']['roles'][0]) #admin

print(type(users['serkanSenturk']['age'])) #int
print(users['serkanSenturk']['roles'][0]) #str


