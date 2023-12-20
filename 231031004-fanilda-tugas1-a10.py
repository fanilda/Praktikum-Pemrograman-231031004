while True:
    try:
        x = int(input('Masukkan Angka (0 Agar Selesai!) : '))
        if x == 0:
            print('Terima kasih')
            break
        elif x % 2 == 0:
             print(f'{x} adalah bilangan GENAP !')
        else:
            print(f'{x} adalah bilangan GANJIL!')
    except ValueError:
        print('Masukkan bilangan yang valid.')                         