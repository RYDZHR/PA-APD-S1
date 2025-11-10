import json
from datajson import baca_data

def registrasi():
    while True:
        data = baca_data()
        member_akun = data["member"]
        try:
            regis_username = input("Masukkan username: ")
            regis_password = input("Masukkan password: ")
            id_akhir = member_akun[-1]["id"]
            if id_akhir != "":
                id_baru = int(id_akhir) + 1
            else:
                id_baru = 1

            if regis_username in [i["username"] for i in member_akun]:
                raise ValueError("Username sudah terdaftar. Silakan coba username lain.")
            elif regis_password.strip() == "":
                raise ValueError("Password tidak boleh kosong.")
            elif regis_username.strip() == "":
                raise ValueError("Username tidak boleh kosong.")
            
            akun_baruM = {
                "id": str(id_baru),
                "username": regis_username,
                "password": regis_password
            }
            member_akun.append(akun_baruM)
            print(member_akun[1:])
            
            with open("file_data/data.json", "w") as file:
                json.dump(data, file, indent = 4 )
                
            print("\nRegistrasi berhasil!")
            input("Tekan Enter untuk kembali...")
            break

        except ValueError as e:
            print(e)
            continue      

      
