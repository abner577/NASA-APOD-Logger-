"""
config.py

Centralized configuration and constant values for the application.
All values defined here are intended to be imported and reused across modules.
"""

import datetime
from pathlib import Path


DIR_PATH = Path(__file__).resolve().parent.parent

DATA_DIR = DIR_PATH / "data"

json_file_path = DATA_DIR / "output.jsonl"
json_file_name = "output.jsonl"

csv_file_path = DATA_DIR / "output.csv"
csv_file_name = "output.csv"

user_settings_path = DATA_DIR / "settings.jsonl"
user_settings_name = "settings.jsonl"

NASA_APOD_START_DATE = datetime.date(1995, 6, 16)
DATE_TODAY = datetime.date.today()