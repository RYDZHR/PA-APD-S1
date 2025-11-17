import inquirer


# MENU YANG DI TAMPILKAN DI AWAL SETELAH LOGIN SEBAGAI ADMIN
def menu_admin():
    menu_awal = [
        inquirer.List("admin_menu",
                      message = "Pilih Salah Satu Menu Yang Tersedia",
                      choices = [
                          "1. Mengelola Data Rute Perjalanan",
                          "2. Mengelola Laporan dan Review Pengguna",
                          "3. Mengelola Akun Pengguna",
                          "4. Logout"
                      ]
                    )   
    ]
    jawab = inquirer.prompt(menu_awal)
    return jawab
    
# MENU YANG DI TAMPILKAN KETIKA ADMIN MEMILIH MENU 1 (MENGELOLA DATA RUTE PERJALANAN)   
def mengelola_rute_perjalanan():
    menu_awal = [
        inquirer.List("menu_pil1",
                        message = "Pilih Salah Satu Menu Yang Tersedia",
                        choices =[
                        "1. Membuat Rute Perjalanan Baru",
                        "2. Melihat Semua Rute Perjalanan",
                        "3. Menghapus Rute Perjalanan",
                        "4. Keluar"
                        ]
                      )
        ]
    jawab_pil1 = inquirer.prompt(menu_awal)
    return jawab_pil1
    