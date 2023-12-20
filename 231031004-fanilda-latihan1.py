
#nilai = 80
#batas_lulus = 70
#if nilai > batas_lulus:
    #print('Selamat, Anda dinyatakan Lulus!')
#else:
    #print('Maaf, Anda dinyatakan Tidak Lulus.')

import hashlib

def hash_password(password):
    # Lapisan 1: Hashing password menggunakan SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def check_password(input_password, hashed_password):
    # Memeriksa apakah password yang dimasukkan sesuai dengan hashed password
    return hash_password(input_password) == hashed_password

def main():
    # Menginisialisasi data mahasiswa
    data_mahasiswa = {
        'username': 'masukkan username',
        'hashed_password': 'ga tau bang'  # Contoh hashed password
    }

    # Meminta mahasiswa untuk memasukkan username dan password
    input_username = input("Masukkan username: ")
    input_password = input("Masukkan password: ")

    # Lapisan 2: Memeriksa username
    if input_username != data_mahasiswa['username']:
        print("Username tidak valid.")
        return

    # Lapisan 3: Memeriksa password
    if not check_password(input_password, data_mahasiswa['hashed_password']):
        print("Password tidak valid.")
        return

    # Jika berhasil melewati semua lapisan, tampilkan pesan selamat datang
    print("Selamat datang, Mahasiswa!")

if __name__ == "__main__":
    main()
