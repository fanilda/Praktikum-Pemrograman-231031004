try:
    operasi = input("Pilih operasi (kurang/tambah): ").lower()
    
    if operasi == "kurang":
        waktu_awal = input("Masukkan waktu awal (Contoh: 12:00) : ")
        jam, menit = map(int, waktu_awal.split(':'))
    
        jam_kurang = int(input("Masukkan jumlah jam yang akan dikurangkan (Contoh: 2): "))
        menit_kurang = int(input("Masukkan jumlah menit yang akan dikurangkan (Contoh: 30) : "))
    
        jam_akhir = (jam - jam_kurang - (menit - menit_kurang) // 60) % 24
        menit_akhir = (menit - menit_kurang) % 60
    
        waktu_akhir = f'{jam_akhir:02d}:{menit_akhir:02d}'
    
        print(f'Waktu sekarang menunjukkan Pukul {waktu_akhir}')
    
    elif operasi == "tambah":
        waktu_awal = input("Masukkan waktu awal (Contoh: 01:00) : ")
        jam, menit = map(int, waktu_awal.split(':'))
    
        jam_tambah = int(input("Masukkan jumlah jam yang akan ditambahkan (Contoh: 2): "))
        menit_tambah = int(input("Masukkan jumlah menit yang akan ditambahkan (contoh: 30) : "))
    
        jam_akhir = (jam + jam_tambah + (menit + menit_tambah) // 60) % 24
        menit_akhir = (menit + menit_tambah) % 60
    
        waktu_akhir = f'{jam_akhir:02d}:{menit_akhir:02d}'
    
        print(f'Waktu sekarang menunjukkan Pukul {waktu_akhir}')
    
    else:
        print("Harap pilih 'kurang' atau 'tambah'.")
except ValueError:
    print('Format jam yang anda masukkan harus lengkap (contoh 12:00)')