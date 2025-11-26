import os, inquirer, prettytable
from file_data.datajson import *

def daftar(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 60)
    print("REVIEW PERJALANAN")
    print("=" * 60)
    data = baca_data_laporan()
    laporan_review = data["review_rute"]
    pertanyaan = [
        inquirer.List('mode',
                     message="Review mana yang ingin dilihat?",
                     choices=['Lihat Review Saya', 'Lihat Semua Review'],
                     ),
    ]
    
    jawaban = inquirer.prompt(pertanyaan)
    perjalanan = []
    for data_review in laporan_review:
        if jawaban['mode'] == 'Lihat Semua Review':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n" + "=" * 60)
            print("SEMUA REVIEW")
            print("=" * 60)
            for i in range(len(data_review["Nama"])):
                perjalanan.append(i)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n" + "=" * 60)
            print(f"REVIEW {username.upper()}")
            print("=" * 60)
            for i in range(len(data_review["Nama"])):
                if data_review["Nama"][i] == username:
                    perjalanan.append(i)
        
        if len(perjalanan) == 0:
            print("\nAnda belum memberikan review.")
            input("Tekan Enter Untuk Kembali...")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print()
            tabel = prettytable()
            tabel.field_names = ["Nama","Nama_Perjalanan", "Destinasi","Tanggal","Durasi","Budget","Cerita","Rating"] 
            for i in perjalanan:
                d = perjalanan[i]
                tabel.add_row([d["Nama"], d["Nama_Perjalanan"], d["Destinasi"], d["Tanggal"], d["Durasi"], d["Budget"], d["Cerita"], d["Rating"]])
            
            print(tabel)  
        
        input("\nTekan Enter untuk kembali...")
        os.system("cls" if os.name == "nt" else "clear")
        return