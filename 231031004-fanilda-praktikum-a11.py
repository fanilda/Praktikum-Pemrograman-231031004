def fibonacci(n):
    if n < 0:
        print('Tidak ada bilangan Fibonacci untuk nilai negatif.')
        return None
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Mengambil input
input_nilai = int(input("Masukkan nilai untuk deret Fibonacci: "))

# pengecekan apakah input_nilai valid (tidak negatif)
if input_nilai < 0:
    print("Nilai harus non-negatif untuk deret Fibonacci.")
else:
    # Menampilkan hasil deret Fibonacci
    hasil = fibonacci(input_nilai)
    if hasil is not None:
        print('Fibonacci(%d) = %d' % (input_nilai, hasil))