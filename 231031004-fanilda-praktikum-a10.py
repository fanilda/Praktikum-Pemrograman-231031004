def faktorial(nilai):
    if nilai <= 1:
        return 1
    else:
        return nilai * faktorial(nilai - 1)

# mencari input
input_nilai = int(input("Masukkan nilai untuk menghitung faktorial: "))

# pengecekan input apakah valid 
if input_nilai < 0:
    print("Faktorial hanya didefinisikan untuk nilai non-negatif.")
else:
    # hasil faktorial
    print('%d ! = %d' % (input_nilai, faktorial(input_nilai)))