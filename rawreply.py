# main.py
from chat import Chat

def reply():
    pengirim = input("Masukkan nama pengirim: ")
    pesan = input("Masukkan balasan: ")
    chat = Chat(pengirim, pesan)

    while True:
        add_more = input("Apakah ingin menambahkan balasan? (y/n): ").strip().lower()
        if add_more == 'y':
            reply_pengirim = input("Masukkan nama pengirim balasan: ")
            reply_pesan = input("Masukkan pesan balasan: ")
            chat.add_reply(reply_pengirim, reply_pesan)
        else:
            break

    print("\nPercakapan:")
    chat.display_pesan()

# Menjalankan fungsi jika file dijalankan secara langsung
if __name__ == "__main__":
    reply()