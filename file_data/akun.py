import json, os
# from datajson import baca_data_akun
from file_data.datajson import baca_data_akun
from pesan import *

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def registrasi():
    while True:
        data = baca_data_akun()
        member_akun = data["member"]
        try:
            regis_username = input("Masukkan username: ")
            regis_password = input("Masukkan password: ")
            banyak_akun = len(member_akun)
            if banyak_akun > 0:
                id_akhir = int(member_akun[-1]["id"])
                id_baru = id_akhir + 1
            else:
                id_baru = 1

            if regis_username in [akun["username"] for akun in member_akun]:
                raise ValueError("Username sudah terdaftar. Silakan coba username lain.")
            elif regis_password.strip() == "":
                raise ValueError("Password tidak boleh kosong.")
            elif regis_username.strip() == "":
                raise ValueError("Username tidak boleh kosong.")
            
            akun_baruM = {
                "id": str(id_baru),
                "username": regis_username,
                "password": regis_password,
                "status": "aktif"
            }
            member_akun.append(akun_baruM)
            print(member_akun[-1])
            
            with open("file_data/data_akun.json", "w") as file:
                json.dump(data, file, indent = 4)
                
            print("\nRegistrasi berhasil!")
            input("Tekan Enter untuk kembali...")
            break

        except ValueError as e:
            print(e)
            continue      

def login_akun():
    kesempatan = 3
    while kesempatan > 0:
        data = baca_data_akun()
        akun_member = data["member"]
        akun_admin = data["admin"]
        try:
            username_input = input("Masukkan username: ").strip()
            password_input = input("Masukkan password: ").strip()
            
            if password_input.strip() == "":
                raise ValueError("Password tidak boleh kosong.")
            elif username_input.strip() == "":
                raise ValueError("Username tidak boleh kosong.")
            
        # Login akun member
            for member in akun_member:
                if username_input == member["username"]:
                    if password_input == member["password"]:
                        if member["status"] == "BANNED":
                            print("Akun anda telah di banned. Silakan hubungi admin untuk mendapat bantuan/Buat akun baru")
                            while True:
                                tanya = input("Apakah anda ingin menghubungi admin sekarang? (y/n): ")
                                if tanya.lower() == 'y':
                                    print("Menghubungi admin...")
                                    detik5()
                                    return None, None
                                # LANJUTKAN INI BIAR USER BISA HUBUNGI ADMIN
                                elif tanya.lower() == 'n':
                                    print("Kembali ke menu utama...")
                                    detik5()
                                    return None, None
                                else:
                                    print("Input harus 'y' atau 'n'. Silakan coba lagi.")
                                    detik3_coba_lagi()
                                    clear()
                                    continue
                        else:
                            return "member", member["id"]
                    else :
                        kesempatan -= 1
                        input("Password salah. Silakan tekan enter untuk coba lagi.")
                        detik3_coba_lagi()
                        break
                         
        # Login akun admin
            for admin in akun_admin:
                if username_input == admin["username"]:
                    if password_input == admin["password"]:
                        return "admin", admin["id"]
                    else:
                        kesempatan -= 1
                        input("Password salah. Silakan tekan enter untuk coba lagi.")
                        detik3_coba_lagi()
                        break
            else:            
                print("Username tidak ditemukan. Silakan registrasi terlebih dahulu.")
                detik5()
                return None, None
            
        except ValueError as e:
            print(e)
            return None, None
            
    print("Kesempatan login habis. Silakan coba lagi nanti.")
    detik5()
    return None, None    
      
