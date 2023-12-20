pw = ['fani', 'fani04', 'fanilda']
kesempatan = 3
a = 0
b = False

while a < len(pw) and not b:
    attempts = 0

    while attempts < kesempatan:
        password = input(f"Silahkan masukkan password {a + 1} Anda : ")
        attempts += 1

        if password == pw[a]:
            print(f"Password {a + 1} yang Anda masukkan benar!")
            a += 1
            break
        else:
            if attempts == kesempatan:
                print("Anda telah melebihi kesempatan yang ditentukan untuk password ini. Anda tidak dapat login.")
                b = True
                break
            else:
                remaining_attempts = kesempatan - attempts
                print(f"Password yang Anda masukkan salah. Anda memiliki {remaining_attempts} percobaan lagi untuk password {a + 1}.")

if a == len(pw) and not b:
    print("Selamat, Anda telah Login!")