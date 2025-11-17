from pack_admin.daftar_kota import kota_awal, kota_tujuan
from prettytable import PrettyTable
from file_data.datajson import *
from pesan import *

import os

def membuat_rute_perjalanan():
    data = baca_data_perjalanan()
    kota_1 = kota_awal()
    
    rute_sudah_ada = [kota["rute"].split("-")[1] for kota in data[kota_1]]
    semua_kota = [kota for kota in data.keys() if kota != kota_1]
    kota_tersisa = [kota for kota in semua_kota if kota not in rute_sudah_ada]
    if not kota_tersisa:
        print(f"\nSemua kota tujuan untuk kota {kota_1} sudah dibuat.")
        print("Tidak ada rute baru yang bisa dibuat dari kota ini.\n")
        input("Tekan Enter untuk kembali ke menu...")
        os.system("cls" if os.name == "nt" else "clear")
        return

    kota_2 = kota_tujuan(kota_1, list_kota = rute_sudah_ada)
    tambah_rute = data[kota_1]
    rute = f"{kota_1}-{kota_2}"
    rute_kebalikan = f"{kota_2}-{kota_1}"
    jarak_otomatis = None

    for daftar_kota in data.values():
        for i in daftar_kota :
            if i["rute"] == rute_kebalikan:
                jarak_otomatis = i["jarak_tempuh"]
                break
        if jarak_otomatis is not None:
            break

    while True:
        if jarak_otomatis is not None:
            jarak_tempuh = jarak_otomatis
            rute_baru = {
                    "rute": rute,
                    "jarak_tempuh": jarak_tempuh,
                    "status" : "aman"
                    }
            tambah_rute.append(rute_baru)
            with open("file_data/data_perjalanan.json", "w") as file:
                json.dump(data, file, indent = 4)
                
            print(f"\nRute Yang Sama Ditemukan ({rute_kebalikan}).")
            print(f"Jarak Otomatis Digunakan: {jarak_tempuh} km\n")
            input("Tekan Enter Untuk Kembali Ke Menu Awal")
            os.system("cls" if os.name == "nt" else "clear")
            break
        
        else:
            jarak_tempuh = input("Masukkan Jarak Tempuh (dalam km): ").strip()
            try:
                jarak_tempuh = float(jarak_tempuh)
                
                if jarak_tempuh <1:
                    print("Jarak Tidak Boleh Minus dan NOL!!")
                    input("Tekan Enter Untuk Menginput Ulang")
                    os.system("cls" if os.name == "nt" else "clear")
                    continue
                    
                rute_baru = {
                    "rute": rute,
                    "jarak_tempuh": jarak_tempuh,
                    "status" : "aman"
                    }
                tambah_rute.append(rute_baru)
                with open("file_data/data_perjalanan.json", "w") as file:
                    json.dump(data, file, indent = 4)
                
                while True:
                    print(f"Rute Perjalanan Baru Telah Ditambahkan: {rute}\n")
                    ulang = input("Apakah Anda Ingin Membuat Rute Baru Lagi? (Y/N)").strip()
                    if ulang.lower() == "y":
                        detik5() 
                        os.system("cls" if os.name == "nt" else "clear")
                        return membuat_rute_perjalanan()
                    elif ulang.lower() == "n":
                        print("\nKembali Ke Menu Awal")
                        detik5() 
                        os.system("cls" if os.name == "nt" else "clear")
                        return
                    else:
                        print("\nMasukan Input Sesuai Intruksi Yang Diberikan!!")
                        detik5()
                        os.system("cls" if os.name == "nt" else "clear")
                        continue
                        
                        
            except ValueError:
                print("Input jarak tempuh tidak valid. Harap masukkan angka saja.")
                input("Tekan Enter Untuk Menginput Ulang")
                os.system("cls" if os.name == "nt" else "clear")
                continue
                
 
def melihat_rute_perjalanan():  
    data = baca_data_perjalanan()
    table = PrettyTable()
    table.field_names = ["Kota Asal", "Rute", "Jarak Tempuh (km)", "Status"]
    for kota_asal, list_rute in data.items():
        if list_rute:
           tampilkan_pertama_kali = True
           for info_rute in list_rute:
               if tampilkan_pertama_kali:
                   table.add_row([kota_asal, info_rute["rute"], info_rute["jarak_tempuh"], info_rute["status"]])
                   tampilkan_pertama_kali = False
               else:
                   table.add_row(["", info_rute["rute"], info_rute["jarak_tempuh"], info_rute["status"]])
        else:
            table.add_row([kota_asal, "-", "-", "-"])
        
    print(table)
    input("Tekan Enter Untuk Kembali Ke Menu Awal")
    os.system("cls" if os.name == "nt" else "clear")
    
    
    
