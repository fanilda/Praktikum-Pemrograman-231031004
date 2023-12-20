nama_karyawan = input ('Masukkan nama karyawan : ')
pendapatan_jumlah = input ('Masukkan jumlah pendapatan : ')
pendapatan = int (pendapatan_jumlah )

print('nama karyawan : ', nama_karyawan)
print('pendapatan karyawan : ', pendapatan)

if pendapatan > 1000 :
    print('status: BERHAK')
else:
    print('status: TIDAK BERHAK')