'''UTS
1. Buat variabel jenis list berikut.
    
    BIO =  ['Nama Lengkap',
            'NIM',
            'Tanggal-Bulan-Tahun Lahir'
            'aktif'
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil'
            'Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu rencana studi mahasiswa']

#(NOTED: sesuaikan dengan data anda)
            
2. Buat variabel jenis nested list berikut.

MK =   [['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216',],
        ['Matkul1','Matkul2','Matkul3','Matkul4','Matkul5','Matkul6','Matkul7','Matkul8'],
        [2,3,3,2,3,3,3,2],
        ['Selasa','Senin','Rabu','Senin','Kamis','Kamis','Kamis','Kamis'],
        ['07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10']]

#(NOTED: Ubah Nama Matakuliah, Jumlah SKS, waktu kuliah, dan jadwal)
        
3. Susun Kode dengan hasil runing seperti berikut.
           
            
             INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE
                             JURUSAN SAINS
                    KARTU RENCANA STUDI MAHASISWA
                           GANJIL 2023/2024

                    
Nama Lengkap    : NAMA LENGKAP
NIM             : 60022010
Program/prodi   : S1/Sistem Informasi A
Tahun Masuk     : 2023 Ganjil
Status          : Aktif
|--|--  10  --|--           26         --|--5--|-- 8  --|--    13   --|
-----------------------------------------------------------------------
No. Kode      |      Mata Kuliah         | SKS |  Hari  |    Jadwal   |
-----------------------------------------------------------------------
1   22A1209   | Matkul1                  |  2  | Senin  |  07.30-09.10|
2   22A1210   | Matkul2                  |  3  | Selasa |  07.30-09.10|
3   22A1211   | Matkul3                  |  3  | Rabu   |  07.30-09.10|
4   22A1212   | Matkul4                  |  2  | Senin  |  07.30-09.10|
5   22A1213   | Matkul5                  |  3  | Kamis  |  07.30-09.10|
6   22A1214   | Matkul6                  |  3  | Kamis  |  07.30-09.10|
7   22A1215   | Matkul7                  |  3  | Kamis  |  07.30-09.10|
8   22A1216   | Matkul8                  |  2  | Kamis  |  07.30-09.10|
-----------------------------------------------------------------------
                        TOTAL SKS           21                        |
-----------------------------------------------------------------------
|---------------------------------71-----------------------------------|
Summary:
Jumlah Mata Kuliah       : 8
Jumlah Mata Kuliah 2 SKS : 3 Mata Kuliah
Jumlah Mata Kuliah 3 SKS : 5 Mata kuliah
Mata Kuliah hari Senin   : 2 Mata Kuliah
Mata Kuliah hari Selasa  : 1 Mata Kuliah
Mata Kuliah hari Rabu    : 1 Mata Kuliah
Mata Kuliah hari Kamis   : 1 Mata Kuliah
Mata Kuliah hari Jumat   : 0 Mata Kuliah
                                              Parepare, 25 Oktober 2023



                                                     NAMA LENGKAP      
                                                     ------------
'''


# Tulis Kode Jawaban di bawah!

bio =  ['FANILDA DAMAYANTI',
            '231031004',
            '05 Maret 2005',
            'aktif',
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil',
            'Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu rencana studi mahasiswa']

mk =   [['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216',],
        ['Pengantar Pemrograman','Kalkulus Dasar I','Sains Terpadu','Bahasa Indonesia','PTI','Wawasan CINTA','Pancasila','Agama Islam'],
        ['3','3','3','2','3','2','2','2'],
        ['Selasa','Selasa','Rabu','Kamis','Kamis','Kamis','Jumat','Jumat'],
        ['07.30-09.10','13.30-15.10','13.30-15.10','07.30-09.10','13.30-15.10','15.20-17.00','09.20-11.00','13.30-15.10']]

print(bio[-4].upper().center(71))
print(bio[-2].upper().center(71))
print(bio[-1].upper().center(71))
strr = bio[-5]+' '+bio[-6].replace('-','/')
print(strr.upper().center(71))

print(f'''
Nama Lengkap    : {bio[0].upper()}
NIM             : {bio[1]}
Program/prodi   : {bio[4]}/{bio[5]}
Tahun Masuk     : {bio[6].title()}
Status          : {bio[3]}''')

print('-'*71)
print('|'+'No.'+'|'+'Kode'.ljust(10)+'|'+'Mata Kuliah'.center(26)+'|'+'SKS'.center(5)+'|'+'Hari'.center(8)+'|'+'Jadwal'.center(13)+'|')
print('-'*71)
print('|'+'1. '+'|'+(mk[0][0]).ljust(10)+'|'+(mk[1][0]).ljust(26)+'|'+(mk[2][0]).center(5)+'|'+(mk[3][0]).center(8)+'|'+(mk[4][0]).center(13)+'|')
print('|'+'2. '+'|'+(mk[0][1]).ljust(10)+'|'+(mk[1][1]).ljust(26)+'|'+(mk[2][1]).center(5)+'|'+(mk[3][1]).center(8)+'|'+(mk[4][1]).center(13)+'|')
print('|'+'3. '+'|'+(mk[0][2]).ljust(10)+'|'+(mk[1][2]).ljust(26)+'|'+(mk[2][2]).center(5)+'|'+(mk[3][2]).center(8)+'|'+(mk[4][2]).center(13)+'|')
print('|'+'4. '+'|'+(mk[0][3]).ljust(10)+'|'+(mk[1][3]).ljust(26)+'|'+(mk[2][3]).center(5)+'|'+(mk[3][3]).center(8)+'|'+(mk[4][3]).center(13)+'|')
print('|'+'5. '+'|'+(mk[0][4]).ljust(10)+'|'+(mk[1][4]).ljust(26)+'|'+(mk[2][4]).center(5)+'|'+(mk[3][4]).center(8)+'|'+(mk[4][4]).center(13)+'|')
print('|'+'6. '+'|'+(mk[0][5]).ljust(10)+'|'+(mk[1][5]).ljust(26)+'|'+(mk[2][5]).center(5)+'|'+(mk[3][5]).center(8)+'|'+(mk[4][5]).center(13)+'|')
print('|'+'7. '+'|'+(mk[0][6]).ljust(10)+'|'+(mk[1][6]).ljust(26)+'|'+(mk[2][6]).center(5)+'|'+(mk[3][6]).center(8)+'|'+(mk[4][6]).center(13)+'|')
print('|'+'8. '+'|'+(mk[0][7]).ljust(10)+'|'+(mk[1][7]).ljust(26)+'|'+(mk[2][7]).center(5)+'|'+(mk[3][7]).center(8)+'|'+(mk[4][7]).center(13)+'|')
print('-'*71)
print('\t\t\t'+'TOTAL SKS'+'  '+'20'.rjust(12))
print('-'*71)

print(f'''
Jumlah Mata Kuliah        : {len(mk[1])}
Jumlah Mata Kuliah 2 SKS  : {len(mk[2][:4])} Mata Kuliah 
Jumlah Mata Kuliah 3 SKS  : {len(mk[2][4:])} Mata Kuliah 
Mata Kuliah Hari Selasa   : {''.join(mk[3]).count('Selasa')} Mata Kuliah
Mata Kuliah Hari Rabu     : {''.join(mk[3]).count('Rabu')} Mata Kuliah
Mata Kuliah Hari Kamis    : {''.join(mk[3]).count('Kamis')} Mata Kuliah
Mata Kuliah Hari Jumat    : {''.join(mk[3]).count('Jumat')} Mata Kuliah
''')
print('Parepare, 25 Oktober 2023'.rjust(71))
print()
print()
print()
print(bio[0].rjust(71-3))
print(('-'*20).rjust(71-3))