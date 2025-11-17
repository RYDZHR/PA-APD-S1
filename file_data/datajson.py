import json

def baca_data_akun():
    with open("file_data/data_akun.json", "r") as file:
        return json.load(file)
    
    
def baca_data_perjalanan():
    with open("file_data/data_perjalanan.json", "r") as file:
        return json.load(file)
    