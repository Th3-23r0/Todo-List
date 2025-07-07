import os

ID_FILE = "id.txt"

def load_id():
    if os.path.exists(ID_FILE):
        with open(ID_FILE, "r") as f:
            return int(f.read())
    else:
        return 0  # start at 0 if no file

def save_id(id_value):
    with open(ID_FILE, "w") as f:
        f.write(str(id_value))