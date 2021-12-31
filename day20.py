print('=' * 20, "LIST", '=' * 20)

#no 1
warna = ['merah', 'kuning', 'hijau', 'biru', 'ungu']
print(warna)
#no 2
banyak_warna = len(warna)
print(banyak_warna)
#no 3
warna[1] = 'jingga'
print(warna)
#no 4
print(warna[0])
#no 5
print(warna[-1])
#no 6
print(warna[2 : 4])
#no 7
warna.append('putih')
print(warna)
#no 8
warna.extend(['pink', 'hitam'])
print(warna)
#no 9
warna.insert(3, 'coklat')
print(warna)
#no 10
del warna[1]
print(warna)
#no 11
warna.remove('biru')
print(warna)
#no 12
warna.pop
print(warna)
#no 13
for wrn in warna :
    print(wrn)


print('=' * 20, "TUPLE", '=' * 20)

#no 1
warna = ('merah', 'kuning', 'hijau', 'biru', 'ungu')
print(warna)
#no 2
banyak_warna = len(warna)
print(banyak_warna)
tinggi_badan
#no 3
w = list(warna)
w[1] = 'jingga'
warna = tuple(w)
print(warna)
#no 4
print(warna[0])
#no 5
print(warna[-1])
#no 6
print(warna[2 : 4])
#no 7
w = list(warna)
w.append('putih')
warna = tuple(w)
print(warna)
#no 8
w = list(warna)
w.extend(['pink', 'hitam'])
print(warna)
#no 9
w = list(warna)
w.insert(3, 'coklat')
print(warna)
#no 10
w = list(warna)
del w[1]
warna = tuple(w)
print(warna)
#no 11
w = list(warna)
w.remove('biru')
warna = tuple(w)
print(warna)
#no 12
w = list(warna)
w.pop
warna = tuple(w)
print(warna)
#no 13
for wrn in warna :
    print(wrn)
