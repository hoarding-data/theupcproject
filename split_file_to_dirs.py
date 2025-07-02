from datetime import datetime
import csv
import shutil
import os
from collections import defaultdict

folder_path = "entries"

def create_entries_folder():
    if os.path.isdir(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)

def save_items_to_csv(digit, items):
    folder_string = f"{folder_path}/{digit}"
    os.makedirs(folder_string)
    with open(f"{folder_string}/{digit}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["upc_a_code","item_name"])  # write header
        writer.writerows(items) 

def main():
    yyyy_mm = datetime.now().strftime("%Y_%m")

    filename = "upc_a_products_{}.csv".format(yyyy_mm)
    with open(filename) as fh:
        data = csv.reader(fh)
        large_list = list(data)
    create_entries_folder()

    first_digit_dict = defaultdict(list)

    #skip header
    for item in large_list[1:]:
        first_digit = item[0][0]
        first_digit_dict[first_digit].append(item)

    for digit, items in first_digit_dict.items():
        save_items_to_csv(digit,items)

if __name__ == "__main__":
    main()



