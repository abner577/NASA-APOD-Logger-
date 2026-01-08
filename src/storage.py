from pathlib import Path
import json
import csv
from test_data import TEST_DATA

DIR_PATH = "C://Users/joser/PycharmProjects/NASA-APOD-Logger"
json_file_path = f"{DIR_PATH}/data/output.json"
csv_file_path = f"{DIR_PATH}/data/output.csv"

print(json_file_path)
print(csv_file_path)


def log_data_to_json(formatted_apod_data):
    if not check_if_json_output_exists():
        print(f"json file {json_file_path} does not exist. Creating it...")
        Path(f"{json_file_path}").touch()

    try:
        with open(file=json_file_path, mode='a', encoding='utf-8') as json_file:
            json.dump(formatted_apod_data, json_file, ensure_ascii=False, indent=4)

    except PermissionError:
        print(f"Dont have permission to write to {json_file_path}.")
    except Exception as e:
        print(e)

def log_data_to_csv(formatted_apod_data):
    if not check_if_csv_output_exists():
        print(f"csv file {csv_file_path} does not exist. Creating it...")
        Path(f"{csv_file_path}").touch()

    try:
        with open(file=csv_file_path, mode='a', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=formatted_apod_data.keys())
            writer.writeheader()
            writer.writerow(formatted_apod_data)

    except PermissionError:
        print(f"Dont have permission to write to {csv_file_path}.")
    except Exception as e:
        print(e)

def check_if_data_exists():
    if Path('../data').is_dir():
        return True
    else:
        return False

def create_data_directory():
    if check_if_data_exists():
        print("Directory 'data' already exists ❌")
        return

    Path(f"{DIR_PATH}/data").mkdir(parents=True, exist_ok=True)
    print("Directory 'data' created ✅")


def check_if_json_output_exists():
    if Path(json_file_path).exists() and Path(json_file_path).is_file():
        print(f"{json_file_path} exists ✅")
        return True

    return False

def check_if_csv_output_exists():
    if Path(csv_file_path).exists() and Path(csv_file_path).is_file():
        print(f"{json_file_path} exists ✅")
        return True

    return False


