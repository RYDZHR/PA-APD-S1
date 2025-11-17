import inquirer, os

def daftar_kota():
    kota = [
            "Balikpapan",
            "Samarinda",
            "Bontang",
            "Banjarbaru",
            "Banjarmasin",
            "Pontianak",
            "Singkawang",
            "Palangkaraya",
            "Tarakan"  
                     ]
    return kota

def kota_awal():
    kota_awal = [
       inquirer.List("kota",
                     message = "Pilih Salah Satu Kota Yang Akan Menjadi Kota Awal Perjalanan ",
                     choices = daftar_kota()
                     
           
       )
   ]
    jawab_awal = inquirer.prompt(kota_awal)
    kota_asal = jawab_awal["kota"]
    os.system("cls" if os.name == "nt" else "clear")
    return kota_asal

def kota_tujuan(kota_asal, list_kota = []):
    kota_tujuan = [
       inquirer.List("kota",
                     message = "Pilih Salah Satu Kota Yang Akan Menjadi Kota Tujuan Perjalanan ",
                     choices = [
                         kota for kota in daftar_kota() if kota != kota_asal and kota not in list_kota
                     ]
                )
    ]
    jawab_tujuan = inquirer.prompt(kota_tujuan)
    kota_destinasi = jawab_tujuan["kota"]
    return kota_destinasi
    
    
    

