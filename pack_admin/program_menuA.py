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
        input("Tekan Enter Untuk Kembali Ke Menu Mengelola Rute Perjalnan...")
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
            input("Tekan Enter Untuk Kembali Ke Menu Mengelola Rute Perjalanan...")
            os.system("cls" if os.name == "nt" else "clear")
            break
        
        else:
            jarak_tempuh = input("Masukkan Jarak Tempuh (dalam km): ").strip()
            try:
                jarak_tempuh = float(jarak_tempuh)
                
                if jarak_tempuh <1:
                    print("Jarak Tidak Boleh Minus dan NOL!!")
                    input("Tekan Enter Untuk Menginput Ulang...")
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
                        print("\nKembali Ke Menu Mengelola Rute Perjalanan")
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
    input("Tekan Enter Untuk Kembali Ke Menu Mengelola Rute Perjalanan")
    os.system("cls" if os.name == "nt" else "clear")
    
    
def melihat_akun_pengguna(konfirmasi_awal = False):
    data = baca_data_akun()
    akun = data["member"]
    
    if len(akun) < 1:
        print("Tidak Ada Akun Pengguna Yang Terdeteksi!!")  
        input("\nTekan Enter Untuk Kembali Ke Menu Mengelola Akun Pengguna...")
        detik3()
        os.system("cls" if os.name == "nt" else "clear")  
                
    table = PrettyTable()
    table.field_names = ["ID Akun", "Username Akun", "Passowrd Akun", "Status Akun"]
    for data_akun in akun:
        table.add_row([data_akun["id"], data_akun["username"], data_akun["password"], data_akun["status"]])
    print(table)
    
    if not konfirmasi_awal:
        pilihan = input("Apakah Anda Ingin Menghapus Akun Dari Daftar Ini? (Y/N)").strip().lower()
        if pilihan == "n":
            print("\nKembali Ke Menu Mengelola Akun Pengguna...")
            detik3()
            os.system("cls" if os.name == "nt" else "clear") 
            
        elif pilihan == "y":
            if len(akun) < 1:
                print("Semua Akun Pengguna Sudah Dihapus!!")  
                input("\nTekan Enter Untuk Kembali Ke Menu Mengelola Akun Pengguna...")
                detik3()
                os.system("cls" if os.name == "nt" else "clear")  
                
            while True:
                os.system("cls" if os.name == "nt" else "clear")  
                print(table)
                akun_hapus = input("Masukan ID Akun Yang Ingin Anda BAN: ").strip()
                try:
                    akun_hapus = int(akun_hapus)
                    akun_dihapus = next((x for x in akun if int(x["id"]) == akun_hapus), None)

                    if akun_dihapus is None:
                        print("\nID tidak ditemukan!")
                        input("Tekan Enter untuk ulangi...")
                        os.system("cls" if os.name == "nt" else "clear")
                        continue
                    
                    else:
                        while True:
                            konfirmasi = input(f"Apakah Anda Yakin Ingin Menghapus Akun {akun_dihapus["username"]}? (Y/N)").strip().lower()
                            if konfirmasi == "y":
                                index = akun.index(akun_dihapus)
                                akun.pop(index)
                                
                                with open("file_data/data_akun.json", "w") as file:
                                    json.dump(data, file, indent = 4)
                                    
                                print(f"\nAkun Dengan Username {akun_dihapus["username"]} Berhasil Dihapus!!")
                                while True:
                                    pilihan = input("Apakah Anda Ingin Menghapus Akun Lagi? (Y/N)").strip().lower()
                                    if pilihan == "y":
                                        return melihat_akun_pengguna(konfirmasi_awal = False)
                                    
                                    elif pilihan == "n":
                                        print("Kembali Ke Menu Mengelola Akun Pengguna...")
                                        detik3()
                                        os.system("cls" if os.name == "nt" else "clear")
                                        return
                                    else:
                                        print("\nMasukkan pilihan Y atau N!")
                                        input("Tekan Enter Untuk Menginput Ulang...")
                                        os.system("cls" if os.name == "nt" else "clear")
                                        continue  

                            elif konfirmasi == "n":
                                print("\nPenghapusan dibatalkan.")
                                input("\nTekan Enter Untuk Kembali Ke Menu Mengelola Akun Pengguna...")
                                os.system("cls" if os.name == "nt" else "clear")
                                return

                            else:
                                print("\nMasukkan pilihan Y atau N!")
                                input("Tekan Enter Untuk Menginput Ulang...")
                                os.system("cls" if os.name == "nt" else "clear")
                                continue
                
                except ValueError:
                    print("\nInput Tidak Valid!! ID Harus Berupa Angka!!")
                    input("Tekan Enter Untuk Menginput Ulang...")
                    detik3()
                    os.system("cls" if os.name == "nt" else "clear")
                    continue
                    

def ban_akun_pengguna():
    data = baca_data_akun()
    akun = data["member"]
    table = PrettyTable()
    
    if len(akun) < 1:
        print("Belum Ada Akun Pengguna Yang Dibuat")  
        input("\nTekan Enter Untuk Kembali Ke Menu Mengelola Akun Pengguna...")
        os.system("cls" if os.name == "nt" else "clear")  
    
    table.field_names = ["ID Akun", "Username Akun", "Passowrd Akun", "Status Akun"]
    for data_akun in akun:
        table.add_row([data_akun["id"], data_akun["username"], data_akun["password"], data_akun["status"]])
        
    while True:
        print(table)
        akun_ban = input("Masukan ID Akun Yang Ingin Anda BAN: ").strip()
        try:
            akun_ban = int(akun_ban)
            akun_diban = next((x for x in akun if int(x["id"]) == akun_ban), None)
            if akun_diban is None:
                print("\nID tidak ditemukan!")
                input("Tekan Enter untuk ulangi...")
                os.system("cls" if os.name == "nt" else "clear")
                continue
            
            else:
               while True:
                konfirmasi = input(f"Apakah Anda Yakin Ingin Menghapus Akun {akun_diban["username"]}? (Y/N)").strip().lower()
                if konfirmasi == "y":
                    akun_diban["status"] = "BANNED"
                    
                    with open("file_data/data_akun.json", "w") as file:
                        json.dump(data, file, indent = 4)
                        
                    print(f"\nAkun Dengan Username {akun_diban["username"]} Berhasil Di BAN!!")
                    input("\nTekan Enter Untuk Kembali Ke Menu Mengelola Akun Pengguna...")
                    os.system("cls" if os.name == "nt" else "clear")  
                    return 

                elif konfirmasi == "n":
                    print("\nBAN dibatalkan.")
                    input("\nTekan Enter Untuk Kembali Ke Menu Mengelola Akun Pengguna...")
                    os.system("cls" if os.name == "nt" else "clear")
                    return

                else:
                    print("\nMasukkan pilihan Y atau N!")
                    input("Tekan Enter Untuk Menginput Ulang...")
                    os.system("cls" if os.name == "nt" else "clear")
                    continue
        
        except ValueError:
            print("\nInput Tidak Valid!! ID Harus Berupa Angka!!")
            input("Tekan Enter Untuk Menginput Ulang...")
            detik3()
            os.system("cls" if os.name == "nt" else "clear")
            continue