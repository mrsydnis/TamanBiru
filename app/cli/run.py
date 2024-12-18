# run.py
import sys
from auth.login import access_login
from auth.register import access_register
def main():
    #mengganti encoding standar menjadi utf-8 agar bisa di run di semua terminal
    sys.stdout.reconfigure(encoding='utf-8')
    print('\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u0b68\u09ce\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510')
    
    while True:
        print('┌───────────────────୨ৎ──────────────────┐')
        print('│ Selamat Datang di Aplikasi Taman Biru │')
        print('│───────────────────────────────────────│')
        print('│   Apakah kamu sudah memiliki akun?    │')
        print('│───────────────────────────────────────│')
        print('│   1. Iya, saya sudah memiliki akun    │')
        print('│  2. Tidak, saya belum memiliki akun   │')
        print('│       3. Keluar dari aplikasi         │')
        print('└───────────────────────────────────────┘')

# user memilih jawaban 1 atau 2     
        masuk = input('Pilih jawaban: ')

# kondisional untuk memilih login atau register
        if masuk == '1' or masuk == 'Iya'.lower():
            access_login('start_login')
            break
        elif masuk == '2' or masuk == 'Tidak'.lower():
            access_register('start_register')
            continue
        elif masuk == '3' or masuk == 'Keluar'.lower():
            print('Terima kasih telah menggunakan aplikasi kami.')
            break
        else:
            print('Pilihan tidak tersedia.')

# menjalankan aplikasi
if __name__ == '__main__':
    main()