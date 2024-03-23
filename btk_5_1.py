#if ve else
"""
if (3>2):
    print('Hoş geldiniz')
if True:
    print('Hoş geldiniz')
#true ya da falselu ifade lazım
if False:
    print('Hoş geldiniz')    #yazdırmaz

isa= True
isb=False
if isa:
    print('okey')
if isb:
    print('not okey')    #basmaz

if isa==True:
    print('okey')
print()

name='aci'
parola='1234'

islogin=(name=='aci')and(parola=='1234')
if islogin:
    print('başarılı')

if (name=='aci')and(parola=='1234'):
    print('okeyyy')
else:
    print('tekrar deneyin')
"""
name =input('isminiz: ')
parola=input('parola: ')
if(name=='aci'):
    if(parola=='1234'):
        print('giriş başarılı')
    else:
        print('parola yanlıs')
else:
    print('kullanıcı adını tekrar giriniz')            
