import json
import os
from json import JSONDecodeError
import matplotlib.pyplot as plt

file_path = "data.json"


def create_file():
    with open(file_path, "w") as file:
        json.dump([], file, indent=4)
        print("No File was found! File was created")
        main_menu()


def add_new_stat(year, month, day, weight, reps):
    if not os.path.exists(file_path):
        create_file()
        return
    with open(file_path, mode="r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
        new_stat = {
                "Year": year,
                "Month": month,
                "Day": day,
                "Weight": weight,
                "Reps": reps
        }
        data.append(new_stat)
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
        print("New Stat was added!")
    main_menu()


def show_stats():
    if not os.path.exists(file_path):
        create_file()
        return
    with open(file_path, mode="r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []



def main_menu():
    main_menu_option = int(input("What would you like to do?\n1. ADD A NEW STAT\n2. SHOW GRAPH"))
    match main_menu_option:
        case 1:
            print("Add Date")
            new_stat_year = int(input("What year? \n"))
            new_stat_month =  int(input("What month (1-12)? \n"))
            new_stat_day = int(input("What day? (1-31)\n"))
            new_stat_weight = float(input("How much kg?"))
            new_stat_reps = int(input("How many reps?"))
            add_new_stat(new_stat_year, new_stat_month, new_stat_day, new_stat_weight, new_stat_reps)
        case 2:
            show_stats()
        case _:
            pass

main_menu()