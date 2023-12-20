print('Tugas Praktikum 3'.center(35))
nama = 'Fanilda Damayanti'
nim  = '231031004'
prodi= 'Sistem Informasi A'
print(f'''
Nama\t: {nama}
NIM\t: {nim}
prodi\t: {prodi}''')

'''Dari beberapa string berikut, buatkan manipulasi kode
agar hasil outpunya sesuai'''

str1 = 'duFort Frankel Von Neumann'
a = str1.upper()
b = a.strip('NEUMANN')
c = ('NEUMANN ')
d = c+b
print(d)
#output: NEUMANN DUFORT FRANKEL VON

str2 = 'duFort Frankel Von Neumann'
a = str2.lower()
print(a[0:1]+a[2:3]+a[15:16],a[19:])
#output: dfv neumann

str3 = 'duFort Frankel Von Neumann'
b=str3.upper()
print(b[0:7],b[2:3],b[15:16],b[10:11])
#output: DUFORT F V N

str4 = 'duFOrt Frankel Von Neumann'
c = str4.lower()
d = c.replace('f','F',1)
print(d[19:20].upper(),d[0:6],d[7:8],d[15:16])
#output: N duFort f v

str5 = 'DuFort Frankel Von Neumann'
a = str5.upper()
b = a.strip('NEUMANN')
c = ('NEUMANN ')
d = b.lower()
print(c+ d[0:1],d[2:3],d[15:16])
#output: NEUMANN d f v

str6 = 'duFort Frankel Von Neumann'
a = str6.upper()
b = a.strip('NEUMANN')
c = ('NEUMANN ')
print(c+b[0:1],b[2:3],b[15:16])
#output: NEUMANN DFV

str7 = '@duFort Frankel Von Neumann$'
a=str7.strip('@,$')
b = a.replace('Neumann','NEUMANN')
print(b)
#output: duFort Frankel Von NEUMANN

str8 = '#duFort@Frankel@Von@Neumann$'
a = str8.strip('#,$')
b = a.replace('@',' ')
print(b)
#output: duFort Frankel Von Neumann

str9 = '@duFort@#^Frankel*#(Von(#(Neumann$'
a = str9.replace('@#^',' ').replace('*#(', ' ').replace('(#(',' ').strip('@,$')
print(a)
#output: duFort Frankel Von Neumann

str10 = '@DUFort@!^FraNkel!1(VoN(!(NeuMann^'
a = str10.replace('@!^', ' ').replace('!1(', ' ').replace('(!(', ' ').strip('@,^')
b = a.lower()
c = b.title()
d = c.replace('D','d').replace('f','F')
print(d)
#output: duFort Frankel Von Neumann