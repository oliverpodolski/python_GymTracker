import json
import os
from json import JSONDecodeError

file_path = "data.json"

def create_file():
    with open(file_path, "w") as file:
        json.dump([], file, indent=4)
        print("File was created")
        main_menu()

def add_new_stat(year, month, day, weight, reps):
    pass

def show_stats():
    pass





def main_menu():
    main_menu_option = int(input("What would you like to do?\n1. ADD A NEW STAT\n2.SHOW GRAPH"))
    match main_menu_option:
        case 1:
            pass
        case 2:
            pass
        case _:
            pass