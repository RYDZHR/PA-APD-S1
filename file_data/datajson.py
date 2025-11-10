import json

def baca_data():
    with open("file_data/data.json", "r") as file:
        return json.load(file)
    