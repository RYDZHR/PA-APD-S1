import json
import inquirer

from pesan import *

while True:
    teks_mulai()
    login = [
        inquirer.List('login',
                      message="Pilih menu",
                     choices=[
                         "Login",
                         "Registrasi",
                         "Keluar"
                     ]
                     )
                      
    ]
    jawab = inquirer.prompt(login)
    
    break
    